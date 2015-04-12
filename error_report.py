# -*- coding: utf-8 -*-

from parsimonious.nodes import NodeVisitor
from parsimonious.grammar import Grammar
from wiktionaryreader import WiktionaryVisitor
import codecs

fl = codecs.open('test-content.txt', 'r', 'utf-8')
content = fl.read()
fl.close()

grammar = Grammar(WiktionaryVisitor.grammar_rules)
print grammar.parse(content)
