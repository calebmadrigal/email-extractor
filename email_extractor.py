#!/usr/bin/env python
import re, sys
email_pattern = re.compile('(\w+[.|\w]\w+@(\w+[.]\w+[.|\w+])\w+)')
data = sys.stdin.read()
matches = re.findall(email_pattern, data)
print ', '.join([match[0] for match in matches])
