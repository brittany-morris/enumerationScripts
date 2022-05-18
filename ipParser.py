#!/usr/bin/env python3
 
import fileinput
import re
import sys
 
file_name = sys.argv[1]
 
with open(file_name, 'r') as f:
    fstring= f.readlines()

for line in fileinput.input():
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
    if ip:
        for i in ip:
            print(i)
