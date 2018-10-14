import urllib
from urllib import request

"""
    内容写入文件
"""
def write_to_file(path,html):
    f=open(path,'w+',encoding='utf-8')
    f.write(str(html.decode('utf-8')))
    f.close()

"""
   获取连接
   @author adi
   @param url 要爬取的地址
   @return 网页源代码 
"""
def load_page(url,headers):
    req=request.Request(url=url,headers=headers)
    response=request.urlopen(req)
    html=response.read()
    return html

"""
    百度贴吧核心爬取程序
    分析其路径，其分页关系存在：当前页的pn等于上一页的页码*50 这样的关系
    @param url 需要做处理的地址
    @param begin 起始页码
    @param end 终止页码
"""
def path_format(url,begin,end):
    # IE 9.0
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'

    headers = {'User-Agent': user_agent}

    for i in range(begin,end+1):
        pn=50*(int(i)-1)
        url2=url+str(pn)
        html=load_page(url2,headers)
        path=str(i)+'.html'
        print("准备写入第"+str(i)+"个页面")
        write_to_file(path,html)

if __name__ == '__main__':
    path_format("http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=",1,5)
