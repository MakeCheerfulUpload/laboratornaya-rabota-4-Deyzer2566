print((367298+8*2)%36)#6
#JSON -> XML
#ВТОРНИК

def fromArrayToXML(l:list,lvl:int):
    ret=''
    for k,j in enumerate(l):
        ret += ' '*lvl+'<elem'+str(k)+'>'
        if type(j) is list:
            ret += '\n'+fromArrayToXML(j,lvl+1)+'\n'+' '*lvl
        elif type(j) is dict:
            ret += '\n'+toXML(j,lvl+1)+'\n'+' '*lvl
        else:
            ret += str(j)
        ret += '</elem'+str(k)+'>' + '\n'
    return ret

def toXML(s:dict,lvl:int):
    ret=''
    for key,value in s.items():
        ret += ' '*lvl+'<'+key+'>'
        if type(value) is dict:
            ret += '\n'+toXML(value,lvl+1)+'\n'+' '*lvl
        elif type(value) is list:
            ret += '\n'+fromArrayToXML(value,lvl+1)+'\n'+' '*lvl
        else:
            ret += value
        ret += '</' + key + '>'+'\n'
    return ret
if __name__=='__main__':
    f = open("расписание.json",encoding='utf-8')
    s = f.read()
    f.close()
    in_str=False
    s=list(s)
    offset=0
    l = len(s)
    for j in range(l):
        if s[j-offset] == '"' and s[j-offset-1] != '\\':
            in_str ^= True
        if s[j-offset] in [' ','\t','\n'] and not in_str:
            del s[j-offset]
            offset+=1
    s=''.join(s)
    #s = parseObject(s[1:])
    s=eval(s)
    print(s['schedule']['lessons'][0])
    s=toXML(s,0)
    #print(s)
    f = open('расписание.xml','w')
    f.write(s)
    f.close()