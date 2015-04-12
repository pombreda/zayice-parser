# -*- coding: utf-8 -*-

import unittest
import wikitextparser


class WikiTextParserTests(unittest.TestCase):

	def test_indexed_list(self):
		test_string = u'[1]: anlam 1 [2]: [tag] anlam 2 [3] anlam 3'
		result = wikitextparser.list_from_brackets(test_string)
		self.assertEqual(len(result), 3)
		self.assertTrue(result[0].find('anlam 1') > -1)
		self.assertTrue(result[1].find('anlam 2') > -1)
		self.assertTrue(result[2].find('anlam 3') > -1)
		test_string = u'text without index'
		result = wikitextparser.list_from_brackets(test_string)
		self.assertEqual(len(result), 1)
		
	
	def test_normalize_square_brackets(self):
		test_string = '[[test]]'
		result = wikitextparser.normalize_square_brackets(test_string)
		self.assertEqual(result, 'test')
		test_string = u'[[yıl|yılın]] xxx [[ay|ayın]]'
		result = wikitextparser.normalize_square_brackets(test_string)
		self.assertEqual(result, u'yılın xxx ayın')


	def test_normalize_curly_brackets(self):
		test_string = u'{{terim|mimarlık}}xxx{{terim}}'
		result = wikitextparser.normalize_curly_brackets(test_string)
		self.assertEqual(result, u'(mimarlık): xxx')

	def test_normalize_brackets(self):
		test_string = u'{{terim|mimarlık}}xxx{{terim}}[[yıl|yılın]] xxx [[ay|ayın]]'
		result = wikitextparser.normalize_brackets(test_string)
		self.assertEqual(result, u'(mimarlık): xxxyılın xxx ayın')

	def test_list_from_brackets(self):
		test_string = u'{{terim|mimarlık}}xxx{{terim}}[[yıl|yılın]] xxx [[ay|ayın]]'
		result = wikitextparser.normalize_brackets(test_string)
		self.assertEqual(result, u'(mimarlık): xxxyılın xxx ayın')




