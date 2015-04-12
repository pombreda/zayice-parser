# -*- coding: utf-8 -*-

from xml.sax import make_parser, ContentHandler
import re
import codecs
import sys
import datetime
from dateutil import parser as date_parser
import time

class WiktionaryParser(ContentHandler):
    currentNode = None
    currentTitle = None
    pageBody = []

    def __init__(self, output_name):
        ContentHandler.__init__(self)
        self.transformedWriter = open(output_name, 'w')
        self.current_timestamp = None
        self.total = 0
        self.skipped = 0
        self.written = 0

    def startDocument(self):
        self.transformedWriter.write(u'<pages>')
        print "document started"

    def startElement(self, name, attrs):
        self.currentNode = name

    def endElement(self, name):
        if(name == "page"):
            body = ''.join(self.pageBody)
            self.total += 1
            if '=={{Dil|Türkçe}}==' in body and self.check_word_type(body):
                page_body = self.page_node()
                self.transformedWriter.write(page_body)
                self.written += 1
                print "Written: " + self.currentTitle
            else:
                self.skipped += 1
                print "Skipped: " + self.currentTitle
            self.pageBody = []

    def endDocument(self):
        self.transformedWriter.write(u'</pages>')
        self.transformedWriter.close()
        self.show_report()

    def characters(self, content):
        content = content.strip().replace('<', '^^(').replace('>', ')^^').replace('nbsp;', '')
        if(len(content) < 2):
            return
        if(self.currentNode == "title"):
            self.currentTitle = content.encode('utf-8')
        if(self.currentNode == "text"):
            self.pageBody.append(content.encode('utf-8'))
        if(self.currentNode == 'timestamp'):
            try:
                self.current_timestamp = time.mktime(date_parser.parse(content).timetuple())
            except ValueError as exc:
                self.current_timestamp = 1

    def check_word_type(self, text):
    	plural_pattern = '{{t|çoğul}}'
    	if plural_pattern in text:
    		return False
    	pattern = re.compile('(=== *{{Söztürü\|([^|]+)\|Türkçe}} *===)')
        matches = pattern.findall(text)
        if len(matches) == 0:
            return False
        if len(matches) == 1 and 'çekilmiş' in matches[0][1]:
            return False

        return True

    def clean_html(self, text):
        return re.sub('\^\^\(([^\^]+)\)\^\^', '', text)


    def page_node(self):
        node = "<page date=\"{2}\" title=\"{0}\">\n{1}\n</page>\n\n"
        body = self.clean_html(''.join(self.pageBody))
        return node.format(self.currentTitle,
                           body, self.current_timestamp)

    def show_report(self):
        print "Total: {0}, Written: {1}, Skipped: {2}".format(self.total, self.written, self.skipped)

if __name__ == '__main__':
    input_name = sys.argv[1]
    output_name = 'filtered.xml' if len(sys.argv) < 3 else sys.argv[2]
    print "Filtering {0} -> {1}".format(input_name, output_name)
    parser = make_parser()
    parser.setContentHandler(WiktionaryParser(output_name))
    parser.parse(input_name)