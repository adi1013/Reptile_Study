import re

def openFile():
    str=''
    with open('save.html','r',encoding='utf-8') as f:
        str=f.read()
        f.close()
    return str

def formatResult(str):
    list=re.findall(r'<tr class="alt">(.*?)</tr>',str,re.S)  #换行符一同匹配
    with open('save3.txt', 'r+', encoding='utf-8') as s2:
        for i in range(len(list)):
            str2=re.findall(r'<td.*?>(.*?)</td>',list[i],re.S)
            str3=str2[1].strip().replace('<div align="left">','').replace('</div>','')
            str2[1]=str3
            for j in range(len(str2)):
                s2.write('{:<15}'.format(str2[j]))
            s2.write('\n')
        s2.close()
    return list

if __name__ == '__main__':
    str=openFile()
    list=formatResult(str)