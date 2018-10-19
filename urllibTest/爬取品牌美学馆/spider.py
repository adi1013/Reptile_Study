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
    def clearData(self,html):
        print('获取网页源代码完毕，准备解析标签路径...')
        #<a.*?><img src="(.*?)"</a>
        str2=re.search(r'<div class="work-list c-fix">(.*)</div>',html,re.S)
        return str2.group(1)

    '''
        @param filename 存入文件名
        @param str 写入字符串
    '''
    def saveToFile(self , filename , str):
        with open(filename ,'r+',encoding='utf-8') as f:
            f.write(str)
            f.close()

    '''
        @param filename 读取文件
    '''
    def getStrFromFile(self , filename):
        with open(filename , encoding='utf-8') as f:
            str = f.read()
            f.close()
        return str

    def secondClear(self):
        fromFile = self.getStrFromFile('save.txt')
        list = re.findall(r'target="_blank">.*?<img src="(.*?)"',fromFile,re.S)
        saveStr=''
        #将图片地址存入文件
        for i in range(len(list)):
            saveStr += list[i]+'\n'
        self.saveToFile('save2.txt' , saveStr)

if __name__ == '__main__':
    spi = spider()
    '''
        获取源代码后进行第一次清洗
    '''
    # html = spi.getResource('http://www.tooopen.com/work/16.aspx')
    # str = spi.clearData(html)
    # spi.saveToFile('save.txt' , str)
    '''
        清洗后将图片路径写入txt文件
    '''
    spi.secondClear()