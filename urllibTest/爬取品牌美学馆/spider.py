#coding=utf-8
from urllib import request
import re

class spider(object):
    def getResource(self,url):
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        req=request.Request(url=url,headers=headers)
        resp=request.urlopen(req)
        print('准备读取网页...')
        html=resp.read()
        return html.decode('utf-8')

    '''
        初步加载
        @param str 源代码
    '''
    def clearData(self,str):
        print('获取网页源代码完毕，准备解析标签路径...')
        #<a.*?><img src="(.*?)"</a>
        str2=re.search(r'<div class="work-list c-fix">(.*)</div>',str,re.S)

    def secondClear(self):
        str=''
        with open('save.txt',encoding='utf-8') as f:
            str=f.read()
            f.close()
        str2=re.search(r'<div class="work-list c-fix">(.*?)</div>',str,re.S)
        list=re.findall(r'<img src="(.*?)"',str2.group(1),re.S)
        print(list)
if __name__ == '__main__':
    spi = spider()
    # html = spi.getResource('http://www.tooopen.com/work/16.aspx')
    # print(html)
    # str = spi.clearData(html)
    # print(str)
    # with open('save.txt','r+',encoding='utf-8') as f:
    #     f.write(str)
    #     f.close()
    spi.secondClear()