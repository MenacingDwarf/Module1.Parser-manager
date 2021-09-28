from bs4 import BeautifulSoup, Tag

def info_extract(isoup):
    tlist = []
    def info_extract_helper(inlist, count = 0):
        if(isinstance(inlist, list)):
            for q in inlist:
                if(isinstance(q, Tag)):
                    if not (str(q).startswith('<script') or str(q).startswith('<style')):
                        info_extract_helper(q.contents, count + 1)
                else:
                    extracted_str = q.strip()
                    if(extracted_str and (count > 1)):
                        tlist.append(extracted_str)
    info_extract_helper([isoup])
    return tlist


if __name__ == '__main__':
    with open('articles/409424.html', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    text = BeautifulSoup(text)
    print(info_extract(text))
