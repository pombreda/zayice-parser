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

def bracketed_items(text):
    pattern = '\[\[([^\]]+)\]\]'
    p = re.compile(pattern)
    match_list = list(p.finditer(text))
    items = []
    for m in match_list:
        items.append(m.group(1))

    return items

def indexed_list(text):
    pattern = '\[(\d+)]'
    return extract_list(text, pattern)


def named_section(text, pattern, name, clear_header = False):
    section_list = extract_list(text, pattern)
    for section_value in section_list:
        sindex = section_value.find(name)
        if sindex >= 0 and sindex < len(pattern):
            if not clear_header:
                return section_value
            else:
                pattern = re.compile(pattern)
                val = pattern.search(section_value)
                return section_value[len(val.group()):].strip()

    return None


def clear_wiki_text(text):
    pattern = re.compile('(\[\[([^\]]+)\]\])')
    it = pattern.findall(text)
    rep = text
    for i in it:
        key = i[0]
        val = i[1]
        val = val[val.find('|')+1:len(val)] if '|' in val else val
        rep = rep.replace(key, val)

    #clear terms
    rep = re.sub('\{\{([^|]+)\|([^\}]+)\}\}', '(\g<2>): ', rep)    
    rep = re.sub('\{\{([^|]+)\|([^\}]+)\|([^\}]+)\}\}', '(\g<3>): ', rep)    
    rep = re.sub('\{\{([^|]+)\|([^\}]+)\|([^\}]+)\|([^\}]+)\}\}', '(\g<4>): ', rep)    
    return rep

def parse_wiki_text(text):
    pass


def index_definition_list(text):
    replaced_list = []
    def_list = indexed_list(text)
    for defn in def_list:
        defn = defn[defn.find(']')+1:]
        replaced_list.append(clear_wiki_text(defn.strip()))

    return replaced_list