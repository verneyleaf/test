# -*- coding:utf-8 -*-

import urllib
import urllib.request


data = {}
data["word"] = "verney"
url_values = urllib.parse.urlencode(data)
print (url_values)
print (type(url_values))

url = "http://www.baidu.com/s?"
url_full = url + url_values

data = urllib.request.urlopen(url_full).read()
print (urllib.request.urlopen(url))
print (type(urllib.request.urlopen(url))) # http.client.HTTPResponse对象
print (type(data))
data = data.decode('UTF-8')
print (type(data))

#f = open("file.txt", "w")
#f.write(data)
f.close()
