# -*- coding:UTF-8 -*-
import urllib.request
import urllib.parse
import re

'''
爬取笑话大全里的内容
'''

def download_joke(request):
    print('download')
    response = urllib.request.urlopen(request)
    print('lalalll')
    content = response.read().decode('gbk')
    print(content)
    return content

def handler_request(page):
    # url = 'http://www.jokeji.cn/hot.asp?me_page=%s'%page
    url = 'http://www.jokeji.cn/hot.asp?me_page=%s'%page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    request = urllib.request.Request(url,headers=headers)
    return request


def handler_a_href(a_href):
    #拼接a链接
    a_href = 'http://www.jokeji.cn'+urllib.parse.quote(a_href)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    request = urllib.request.Request(a_href,headers=headers)
    content = urllib.request.urlopen(request).read().decode('gbk')
    #提取指定的内容。并且返回
    pattern = re.compile(r'<span id="text110">(.*?)</span>', re.S)
    ret = pattern.findall(content)
    print(ret)
    # 将匹配的内容返回
    if len(ret)!=0:
        return ret[0]
    return None


def parse_content(content):
    print('111111')
    pattern = re.compile(r'<a href="(.*?)" class="main_14" target="_blank">(.*>?)</a>')
    a_title_list = pattern.findall(content)
    print(a_title_list,'=====')

    for a_title in a_title_list:
        print(a_title,'fdsafsda')
        # 获取a链接
        a_href = a_title[0]
        print(a_href)
        # 获取标题
        title = a_title[1]
        print(title)
        #想指定a链接发送请求并且处理得到内容
        content = handler_a_href(a_href)
        print('content',content)
        joke = '<h1>%s</h1><p>%s</p>'%(title,content)
        print('joke',joke)
#         写入文件
        with open('joke.html','a') as f:
            f.write(joke)

def main():
    start = 1
    end = 3
    for page in range(start,end+1):
        request = handler_request(page)
        print(request)
        content = download_joke(request)
#         处理数据
        parse_content(content)


if __name__ == '__main__':
    main()