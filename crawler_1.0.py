# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
from collections import deque

def savedata(data):
	with open("file_save.txt", "w+") as f:
		for i in data:
			f.write(i+"\n")

q = deque([]) #创建空队列
s = set() #创建空集合

url_start = "http://news.dbanotes.net"
q.append(url_start)
cnt = 1
#with open("file_save.txt", "w+") as f:
#	f.write(url_start+"\n")

while (q):
#	if cnt >= 100:
#		break
	url = q.popleft()
	s |= {url}
	if len(s) >= 5:
		break

	try:
		page = urllib.request.urlopen(url, timeout=2)
		if 'html' not in page.getheader('Content-Type'):
			continue

		data = page.read().decode('utf-8')
	except:
		continue
	linkre = re.compile('href="(.+?)"')
	for x in linkre.findall(data):
		if "http" in x and x not in s:
			cnt += 1
		#	if cnt >= 100:
		#		break
#			with open("file_save.txt", "a+") as f:
#				f.write(x+"\n")
			q.append(x)
	print (cnt)
savedata(s)
