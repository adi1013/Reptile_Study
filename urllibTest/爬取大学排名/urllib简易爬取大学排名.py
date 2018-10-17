import re
from urllib import request
'''
   爬虫类
'''
class spider:

    def load_page(self):
        url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
        headers={
            'User_Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
        }
        req=request.Request(url=url,headers=headers)
        response=request.urlopen(req)
        html=response.read()
        return html.decode()

    def save_in_file(self,html):
        with open('save.html','r+',encoding='utf-8') as f:
            f.write(html)
            f.close()

if __name__ == '__main__':
    spi = spider()
    html=spi.load_page()
    spi.save_in_file(html)