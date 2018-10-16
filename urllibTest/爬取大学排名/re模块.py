import re
#第一次接触re模块
def openFile():
    str=''
    with open('save.html','r',encoding='utf-8') as f:
        str=f.read()
        f.close()
    return str

def formatResult(str):
    pattern=re.compile(r"<tr(.*?)>(.*?)</tr>") #<tr.*><td.*>.*?</td></tr>
    list=pattern.findall(str)

    return list

if __name__ == '__main__':
    str=openFile()
    list=formatResult(str)
    for i in range(0,len(list)):
        print(list[i])