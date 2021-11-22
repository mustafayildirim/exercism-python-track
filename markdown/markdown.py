import re

def make_it_strong(first, second, third):
    return first + '<strong>' + second + '</strong>' + third

def make_it_em(first, second, third):
    return first + '<em>' + second + '</em>' + third

def make_it_li(curr):
    return f'<li>{curr}</li>'


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('#{1,6} (.*)', i) is not None:
            splitted = i.split()
            len_of_hash_pound = len(splitted[0])
            i = f'<h{len_of_hash_pound}>' + i[len_of_hash_pound+1:] + f'</h{len_of_hash_pound}>'
        m = re.match(r'\* (.*)', i)
        if m:
            curr = m.group(1)
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                curr = make_it_strong(m1.group(1), m1.group(2), m1.group(3))
            m1 = re.match('(.*)_(.*)_(.*)', curr)
            if m1:
                curr = make_it_em(m1.group(1), m1.group(2), m1.group(3))
            if not in_list:
                in_list = True
                i = '<ul>'+ make_it_li(curr=curr)
            else:
                i = make_it_li(curr=curr)
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = f'<p>{i}</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = make_it_strong(m.group(1), m.group(2), m.group(3))
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = make_it_em(m.group(1), m.group(2), m.group(3))
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
