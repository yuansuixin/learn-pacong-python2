# -*- coding:UTF-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar

#可以保存cookie
cj = http.cookiejar.CookieJar()
#通过这个对象创建handler
handler = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(handler)

post_url = 'https://passport.weibo.cn/sso/login'
data = {
	'username': '17701256561',
	'password': 'lizhibin666',
	'savestate': '1',
	'r': 'http%3A%2F%2Fweibo.cn%2F',
	'ec': '0',
	'pagerefer': '',
	'entry': 'mweibo',
	'wentry': '',
	'loginfrom': '',
	'client_id': '',
	'code': '',
	'qq': '',
	'mainpageflag': '1',
	'hff': '',
	'hfp': '',
}

data = urllib.parse.urlencode(data).encode()
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
# 一般登录都要求使用referer
	'Referer': 'https://weibo.cn/'
}
request = urllib.request.Request(post_url,headers=headers)
# opener里面带了cookie
response = opener.open(request,data=data)
print(response.read().decode())

#访问登录后的页面
url = 'https://weibo.cn/6388179289/info'

request = urllib.request.Request(url=url, headers=headers)

response = opener.open(request)
# 显示登录后的页面是否成功
print(response.read().decode())

