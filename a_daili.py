# -*- coding:UTF-8 -*-
import urllib.request
import urllib.parse

handler = urllib.request.ProxyHandler({
    'http':'122.114.31.177:8888'
})

opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)

response = opener.open(request)
with open('ip.html','wb') as f:
    f.write(response.read())