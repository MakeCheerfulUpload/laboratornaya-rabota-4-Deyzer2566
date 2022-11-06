import json,xmltodict
print((367298+8*2)%36)#6
#JSON -> XML
#ВТОРНИК
if __name__=='__main__':
    with open('расписание.json',encoding='utf-8') as f:
        s = json.loads(f.read())
    # print(s['lessons'][1]['week-num'])
    s = {'root':s}
    with open("расписание.xml", "w",encoding='utf-8') as outf:
        s = xmltodict.unparse(s, pretty=True)
        outf.write(s)