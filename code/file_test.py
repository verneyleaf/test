# -*- coding:utf-8 -*-
s = "hello world!"
with open("file_text1.txt", "w" ) as f1:	
	f1.write(s)
with open("file_text1.txt", "a+") as f2:
	f2.write("\n")
	f2.write(s)
