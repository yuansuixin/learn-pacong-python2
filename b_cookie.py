# -*- coding:UTF-8 -*-
import urllib.request
import urllib.parse

url = 'https://weibo.cn/6388179289/info'

headers = {
'Host': 'weibo.cn',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Referer': 'https://weibo.cn/',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': '_T_WM=b3c4bb70390fce1c3349800bc3fe0551; SUB=_2A253tbCIDeRhGeBN41oQ9yfOwzWIHXVVWdDArDV6PUJbkdAKLXHZkW1NRAKzwXwSAZYDuwAaz8Bj71OHktpzUQWK; SUHB=0xnCSd5W9qthYA; SCF=As5Af8ibRQnCm-k2medatY5GaUB47gh6tX_xaMnpS61ONu9V-FYU6_16zzRAsQe40sfftQoOvR-UptegViHa5qI.; SSOLoginState=1521598680'

	}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())







