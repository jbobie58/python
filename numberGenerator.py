#!/usr/bin/python

def checkNum(maxNum=101):
    for i in range(maxNum):
          value = ""
          if i % 3 == 0: 
            value += "foo"
          if i % 5 == 0: 
            value += "bar"
          yield value if value else i
for num, str1 in enumerate(checkNum()):
    print ("%s: %s" % (num, str1))
