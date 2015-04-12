# -*- coding: utf-8 -*-

import re

def extract_list(text, pattern):
    p = re.compile(pattern)
    result_list = []
    match_list = list(p.finditer(text))
    length = len(match_list)
    j = 0
    for m in match_list:
    	start_index = m.start()
        if j == length - 1:
            end_index = len(text)
        else:
            end_index = match_list[j+1].start()
        result_list.append(text[start_index:end_index])
        j = j+1

    return result_list

def indexed_list(text):
    pattern = '\[(\d+)]'
    return extract_list(text, pattern)

def list_from_brackets(text):
    replaced_list = []
    def_list = indexed_list(text)
    if(len(def_list) == 0):
        return [text]
    for defn in def_list:
        defn = defn[defn.find(']')+1:]
        replaced_list.append(defn.strip())

    return replaced_list

def clean_wiki_text(text):
    return normalize_brackets(text)

def normalize_brackets(text):
    return normalize_square_brackets(normalize_curly_brackets(text))

def normalize_square_brackets(text):
	pattern = re.compile('(\[\[([^\]]+)\]\])')
	it = pattern.findall(text)
	rep = text
	for i in it:
		key = i[0]
		val = i[1]
		val = val[val.find('|')+1:len(val)] if '|' in val else val
		rep = rep.replace(key, val)

	return rep

def normalize_curly_brackets(text):
	rep = re.sub('\{\{([^|]+)\|([^\}]+)\}\}', '(\g<2>): ', text)
	rep = re.sub('\{\{([^|]+)\|([^\}]+)\|([^\}]+)\}\}', '(\g<3>): ', rep)
	rep = re.sub('\{\{([^|]+)\|([^\}]+)\|([^\}]+)\|([^\}]+)\}\}', '(\g<4>): ', rep)
	rep = re.sub('\{\{([^|]+)\}\}', '', rep)
	return rep


