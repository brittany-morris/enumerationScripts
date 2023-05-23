#!/usr/bin/env python3

import sys


file_name = sys.argv[1]
file_name2 = sys.argv[2]
allowList = []
dataList = []
duplist=[]


with open(file_name) as f:
    for line in f:
        x = line.split("\n")[0]
        allowList.append(x)

with open(file_name2) as g:
    for line in g:
        y = line.split("\n")[0]
        dataList.append(y)

for item in dataList:
    if item[-1] == '/': item = item[:-1]
    if item not in allowList: duplist.append(item)

for allowURL in allowList:
    for compareURL in duplist[:]:
        if allowURL[0] == '*':
            if allowURL[1:] in compareURL:
                duplist.remove(compareURL)



sourceFile = open('results.txt', 'w')
print(*duplist, sep = "\n", file = sourceFile) 
sourceFile.close()
