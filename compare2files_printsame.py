#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
file_name2 = sys.argv[2]
list1 = []
list2 = []
duplist=[]

with open(file_name) as f:
    for line in f:
        x = line.split("\n")[0]
        list1.append(x)

with open(file_name2) as g:
    for line in g:
        y = line.split("\n")[0]
        list2.append(y)

for item in list1:
    for item1 in list2:
        if item == item1:
            duplist.append(item)

print(*duplist, sep = "\n")
