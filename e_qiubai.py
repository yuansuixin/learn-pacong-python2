# -*- coding:UTF-8 -*-

import urllib.request
import urllib.parse
import os
import re

'''
获取到糗事百科中的图片
'''

def handler_request(page):
    # 拼接出来指定的url
    url = 'https://www.qiushibaike.com/pic/page/%s/'% page
#     构建请求对象
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    request = urllib.request.Request(url,headers=headers)
    return request


def download_image(request):
    dirname = '糗图'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    response = urllib.request.urlopen(request)
    content = response.read().decode()
    parse_content(content,dirname)

def parse_content(content,dirname):
    # 需要多行匹配，.不能匹配换行符
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=.*?>.*?</div>',re.S)
    image_list = pattern.findall(content)
    # print(image_list)
    for image in image_list:
        # 简单处理图片链接
        image = 'http:'+image
#         获取图片的名字
        image_name = os.path.basename(image)
#         获取文件路径
        image_path = os.path.join(dirname,image_name)
#         下载图片
        urllib.request.urlretrieve(image,filename=image_path)


def main():
    start = 1
    end = 5

    for page in range(start,end+1):
        request = handler_request(page)
        print('正在下载。。。第',page,'页')
        download_image(request)
        print('下载。。。完成。第', page, '页')


if __name__ == '__main__':
    main()


