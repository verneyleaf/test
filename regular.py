# -*- coding:utf-8 -*-

import re

s = 'cats are smarter than dogs'
result = re.match(r'(.*) are (.*?) (.*)', s)
print (result)
print ('\n')
print (type(result.group()))
#if type(result.group()) == 'str':
print (len(result.group()))
print (result.group(0))
print (result.group(1))
print (result.group(2))
print (result.group(3))



print ('\n' + result.group())
