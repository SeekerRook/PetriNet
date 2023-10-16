
def dictionarize(data) -> dict:
    res = {}
    for i in data:

        try:
            if i[0] in res:
                print("Duplicate Element", i )
                exit
            res[i[0]] = int(i[1])

        except TypeError :
            if i in res:
                print("Duplicate Element", i )
                exit
            res[i] = 1
    return res

def frommermaid(s,mode="byName"):
    import re
    re_places = re.compile("[^|\W][^\W]*\(\(.*\)\)")
    re_transistions = re.compile("[^|\W][^\W]*\[.*\]")
    re_arches = re.compile(".*-->.*")

    raw_p = re_places.findall(s)
    raw_t = re_transistions.findall(s)
    raw_a = re_arches.findall(s)
    # print(raw_p)
    # print(raw_t)
    # print(raw_a)
    places_dict = {}
    for i in raw_p:
        places_dict[i.replace("))",'').split('((')[0]] = i.replace("))",'').split('((')[1].replace('"','')
    transitions_dict = {}
    for i in raw_t:
        transitions_dict[i.replace("]",'').split('[')[0]] = i.replace("]",'').split('[')[1].replace('"','')
    clean_a = [re.sub("\[.*\]|\(\(.*\)\)|\t| ",'',i) for i in raw_a] 

    arches = []
    for i in clean_a:
        try:
            n = i.split('|')[1].replace('"','')
            i = re.sub('\|.*\|','',i)
        except IndexError:
            n = 1
        f ,t = i.split('>')
        f = f.replace('-','')
        arches.append([f,t,n])
    if mode == 'byID':
        return list(places_dict.keys()),list(transitions_dict.keys()),arches
    elif mode == 'byName':
        arches_n = []
        for i in arches:
            arches_n.append([places_dict[i[0]] if  i[0] in places_dict else transitions_dict[i[0]],places_dict[i[1]] if  i[1] in places_dict else transitions_dict[i[1]], i[2]])
        return list(places_dict.values()),list(transitions_dict.values()),arches_n
    else: return [],[],[]