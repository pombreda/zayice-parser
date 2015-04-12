# -*- coding: utf-8 -*-
import wikitextparser
from wiktionaryreader import WiktionaryVisitor
from xml.sax import make_parser, ContentHandler
import codecs
import json
import random
import sys
from parsimonious.exceptions import IncompleteParseError
import logging
import os.path

class WiktionaryXmlParser(ContentHandler):

	def __init__(self, output_file, limit = 0, random_mode = False):
		ContentHandler.__init__(self)
		self.total = 0
		self.processed = 0
		self.skipped = 0
		self.skip_version = 0
		self.error = 0
		self.limit = limit
		self.current_node = None
		self.current_title = None
		self.page_body = []
		self.random_mode = random_mode
		self.version_store = WiktionaryVersionStore('version.txt')
		self.writer = codecs.open(output_file, 'w', 'utf-8')
		logging_stream = codecs.open('wiktionary-error.log', 'w', 'utf-8')
		logging.basicConfig(stream=logging_stream, level=logging.DEBUG)

	def startDocument(self):
		self.show_info()
		self.version_store.load_store()
		self.write_open_tag()

	def endDocument(self):
		self.finish_up()

	def startElement(self, name, attrs):
		self.current_node = name
		if(self.current_node == 'page'):
			self.page_body = []
			self.current_title = attrs.getValue('title')
			self.current_timestamp = float(attrs.getValue('date'))

	def endElement(self, name):
		if(name == 'page'):
			"""
			random mode for testing purposes
			"""
			self.total += 1

			if self.current_timestamp <= self.version_store.get_version(self.current_title):
				print "Skipped older version: %s" % self.current_title
				self.skip_version += 1
				return

			if self.random_mode:
				if random.randint(1, 3) % 3 != 0:
					self.skipped += 1
					print "Skipped: %s" % self.current_title
					return

			visitor = WiktionaryVisitor()
			try:
				content = u''.join(self.page_body)
				visitor.parse(content)
				visitor_data = visitor.result
				if 'definitions' not in visitor_data:
					print "Empty: %s" % content
					return

				word_data = {"title": self.current_title}

				for key in visitor_data:
					word_data[key] = self.clean_list(visitor_data[key])

				self.writer.write(json.dumps(word_data, ensure_ascii=False))
				self.writer.write(',')
				self.processed += 1
				print u"Processed :{0} - {1}".format(self.current_title, self.processed)
				self.version_store.set_version(self.current_title, self.current_timestamp)

				if self.limit != 0 and self.processed >= self.limit:
					print u'Exiting...'
					self.finish_up()
					sys.exit(0)

			except IncompleteParseError as exc:
				self.error += 1
				print u"parse error: %s" % self.current_title
				logging.error('Peg parse error: ')
				


	def characters(self, content):
		content = content.strip()
		if(self.current_node == 'page' and len(content) > 0):
			self.page_body.append(content)


	def escape_element_value(self, value):
		return value.replace('"', '\\"')

	def clean_list(self, text):
		return map(lambda x: wikitextparser.clean_wiki_text(x), wikitextparser.list_from_brackets(text))

	def write_open_tag(self):
		self.writer.write('[')

	def write_close_tag(self):
		self.writer.write('{}]')
		self.writer.close()

	def finish_up(self):
		self.version_store.save()
		self.write_close_tag()
		self.show_report()

	def show_info(self):
		print "Starting with limit: {0}, random mode: {1}".format(self.limit, self.random_mode)

	def show_report(self):
		print "Total {0}, processed: {1}, skipped: {2}, error: {3}, old-version:{4}, sub-total: {5}".format(self.total, self.processed, self.skipped, self.error, self.skip_version, (self.processed + self.skipped + self.error))


class WiktionaryVersionStore:

	def __init__(self, file_name):
		self.file_name = file_name
		self.versions = {}

	def load_store(self):
		if not os.path.exists(self.file_name):
			return
		file_stream = codecs.open(self.file_name, 'r', 'UTF-8')
		for line in file_stream:
			values = line.split('\t')
			if len(values) > 1:
				self.versions[values[0]] = float(values[1])
		file_stream.close()

	def get_version(self, name):
		return self.versions[name] if name in self.versions else 0

	def set_version(self, name, value):
		self.versions[name] = float(value)

	def save(self):
		write_stream = codecs.open(self.file_name, 'w', 'UTF-8')
		for key,value in self.versions.iteritems():
			write_stream.write(u'%s\t%f\n' % (key, value))

		write_stream.close()

	def __del__(self):
		pass


if __name__ == '__main__':
	input_file = sys.argv[1]
	output_file = 'terms.json' if len(sys.argv) < 3 else sys.argv[2]
	limit = 0 if len(sys.argv) < 4 else sys.argv[3]
	random_mode = False if len(sys.argv) < 5 or sys.argv[4] != 'true' else True

	parser = make_parser()
	parser.setContentHandler(WiktionaryXmlParser(output_file, int(limit), random_mode))
	parser.parse(input_file)
