#!/usr/bin/python
import re, os, sys
#regular expression that match any strings that are 10-digit phone numbers (e.g. 215-956-8000) 

phoneNum = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print (phoneNum.search('215-956-8000').group())
