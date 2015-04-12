# -*- coding: utf-8 -*-

from parsimonious.nodes import NodeVisitor
from parsimonious.grammar import Grammar


class Tags:
	"enum implementation"
	Definitions, Origins, Synonyms, Antonyms, Proverbs, Idioms, Categories, Undefined = range(8)


class WiktionaryVisitor(NodeVisitor):

	ALLOWED_LANGUAGES = [u'Türkçe']

	grammar_rules = u"""
		wiki_text = wiki_block+
    	wiki_block = language_section_header / section_content / turkce_wordtype_header / subsection_content / definitions_section / origin_section  / synonyms_section  / antonyms_section / proverbs_section  / idioms_section / categories_section / template_content / square_template_content / body / body_text
	    language_section_header = section_open "Dil|" body section_close
	    non_utf_turkce = "T" utf_char_replacement "rk" utf_char_replacement "e"
	    utf_char_replacement = ~"[^\}]"
	    section_content = section_open template_inline section_close
	    section_open = "-"* "=={{" "-"*
	    section_close = "-"* "}}==" "-"*
	    turkce_wordtype_header = subsection_open turkce_wordtype_name subsection_close
	    turkce_wordtype_name = ~"S[^}]zt[^}]r[^}]\|([^\}]+)"
	    subsection_content = subsection_open body subsection_close
	    subsection_open = "==={{"
	    subsection_close = "}}==="
	    square_template_content = square_template_open square_template_body square_template_close
	    square_template_open = "[["
	    square_template_close = "]]"
	    square_template_body = square_template_inline* square_template_content* square_template_inline*
	    square_template_inline = ~"(([^\[\]])|(?<!\[)\[(?!\[)|(?<!\])\](?!\]))+"
	    definitions_section = template_open "Anlamlar" template_close
	    origin_section = template_open ~"K[^}]ken" template_close
	    synonyms_section = template_open ~"E[^}] Anlaml[^}]lar" template_close
	    antonyms_section = template_open ~"Kar[^}][^}]t Anlaml[^}]lar" template_close
	    proverbs_section = template_open ~"Atas[^}]zler" template_close
	    idioms_section = template_open "Deyimler" template_close
	    categories_section = template_open ~"[^}]st Kavramlar" template_close
	    template_content = template_open template_inline template_close
	    template_inline = (~"[^\{\}]*" template_content* ~"[^\{\}]*")+
	    template_open = "{{"
	    template_close = "}}"
	    body = ~"[^\{\}]*"
	    body_text = ~".+"
	"""

	grammar = Grammar(grammar_rules)
	
	def __init__(self):
		self.result = {}
		self.tag = None
		self.language_name = None

	def set_result(self, key, value):
		if(key not in self.result):
			self.result[key] = value
		else:
			self.result[key] += value


	def generic_visit(self, node, visited_children):
		return None

	def visit_language_section_header(self, node, params):
		section_open, prefix, language_name, section_close = params
		self.language_name = language_name

	def visit_wiki_text(self, wiki_block, children):
		self.wiki_text = wiki_block

	def visit_body(self, node, children):
		key_map = {Tags.Definitions: 'definitions', Tags.Synonyms: 'synoynms', Tags.Antonyms: 'antonyms', Tags.Origins: 'origins', Tags.Proverbs: 'proverbs', Tags.Idioms: 'idioms', Tags.Categories: 'categories'}

		if(self.tag in key_map):
			self.set_result(key_map[self.tag], node.text)
		
		return node.text

	def visit_template_content(self, node, params):
		if(node.text.find('|') == -1):
			self.tag = Tags.Undefined

	def tag_template(self, template_tag):
		if(self.language_name in self.ALLOWED_LANGUAGES):
			self.tag = template_tag

	def visit_definitions_section(self, node, (opentag, name, closetag)):
		self.tag_template(Tags.Definitions)

	def visit_synonyms_section(self, node, params):
		self.tag_template(Tags.Synonyms)

	def visit_antonyms_section(self, node, params):
		self.tag_template(Tags.Antonyms)

	def visit_origin_section(self, node, params):
		self.tag_template(Tags.Origins)

	def visit_proverbs_section(self, node, params):
		self.tag_template(Tags.Proverbs)

	def visit_idioms_section(self, node, params):
		self.tag_template(Tags.Idioms)

	def visit_categories_section(self, node, params):
		self.tag_template(Tags.Categories)




