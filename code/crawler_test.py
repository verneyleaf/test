# -*- coding:utf-8 -*-
import urllib.request
import re

url = "http://baidu.com"

page = urllib.request.urlopen(url)

data = page.read().decode('utf-8')

print (data)

linkre = re.compile('http:(.+?)"')
x = linkre.findall(data)
print (x)

###### 我是分割线 ##############
print ("######### 我是分割线 ###########")
content = 'hello world href="www.baidu.com"'
link = re.compile('href="(.+?)"')
y = link.findall(content)
print (y)
