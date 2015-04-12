# -*- coding: utf-8 -*-
from wiki_text_parser import *
from xml.sax import make_parser, ContentHandler
import codecs
import json

class WiktionaryFormatter(ContentHandler):

    currentNode = None
    currentTitle = None
    pageBody = []
    total_articles = 0
    transformedWriter = open("formatted-data.json", 'w')

    def startDocument(self):
        self.transformedWriter.write('{"words":[')
        

    def endDocument(self):
        self.transformedWriter.write('{} ]}')
        self.transformedWriter.close()
        

    def startElement(self, name, attrs):
        self.currentNode = name
        if name == 'page':
            self.currentTitle = attrs.getValue('title').encode('utf-8')

    def endElement(self, name):
        if self.currentNode == 'page':
            body = ''.join(self.pageBody).encode('utf-8')
            lang_specific = named_section(body, '== *{{Dil\|([^|]+)}} *==',
                                                'Türkçe')
            print str(self.total_articles) + " - " + self.currentTitle

            definitions = []
            related_words = {}
            origins = []

            word_types = extract_list(lang_specific,
                                      '=== *{{Söztürü\|([^|]+)\|Türkçe}} *===')
            for word_type in word_types:
                definition_section = named_section(word_type,
                                                   '{{([^|}]+)}}', 'Anlamlar')
                if definition_section is None:
                    continue

                definitions = definitions \
                            + index_definition_list(definition_section)

                proverbs = named_section(word_type, '{{([^|}]+)}}', 'Atasözler', True)
                idioms = named_section(word_type, '{{([^|}]+)}}', 'Deyimler', True)

                synoynms = named_section(word_type,
                                         '{{([^|}]+)}}', 'Eş Anlamlılar', True)
                antonyms = named_section(word_type, '{{([^|}]+)}}', 'Karşıt Anlamlılar', True)
                categories = named_section(word_type, '{{([^|}]+)}}', 'Üst Kavramlar', True)
                origin = named_section(word_type, '{{([^|}]+)}}', 'Köken', True)

                if proverbs is not None:
                    proverb_list = bracketed_items(proverbs)
                    self.append_named_list(related_words, 'proverbs', '|||'.join(proverb_list))

                if idioms is not None:
                    idiom_list = bracketed_items(idioms)
                    self.append_named_list(related_words, 'idioms', '|||'.join(idiom_list))
                
                if synoynms is not None:
                    synonym_list = bracketed_items(synoynms)
                    self.append_named_list(related_words, 'synoynms', '|||'.join(synonym_list))

                if antonyms is not None:
                    antonym_list = bracketed_items(antonyms)
                    self.append_named_list(related_words, 'antonyms', '|||'.join(antonym_list))

                if categories is not None:
                    category_list = bracketed_items(categories)
                    self.append_named_list(related_words, 'categories', '|||'.join(category_list))


                if origin is not None:
                    origins.append(clear_wiki_text(origin))

            definitons_value = '|||'.join(definitions)
            related_list = {}

            for key in related_words.keys():
                r = []
                for item in related_words[key]:
                    r.append(item)

                related_list[key] = r


            related_words_value = json.dumps(related_list, ensure_ascii=False)
            origins_value = '|||'.join(origins)

            node_value = self.page_element(self.currentTitle, definitons_value, related_words_value, origins_value)
            self.transformedWriter.write(node_value)
            self.total_articles += 1
            self.pageBody = []
            self.currentTitle = None
            self.currentNode = None


    def characters(self, content):
        content = content.strip()
        if(len(content) < 1):
            return
        if(self.currentNode == "page"):
            self.pageBody.append(content)


    def escape_element_value(self, value):
        value = value.replace('"', '\\"')
        return '"' + value + '"'


    def page_element(self, title, definitions, related, origin):
        node = {'t':title, 'd':definitions, 'r':related, 'o':origin}
        return json.dumps(node, ensure_ascii = False) + ","

    def append_named_list(self, dict_to_update, key_name, list_to_add):
        if not key_name in dict_to_update:
            dict_to_update[key_name] = []

        dict_to_update[key_name].append(list_to_add)


parser = make_parser()
parser.setContentHandler(WiktionaryFormatter())
parser.parse("pages-in-language.xml")
