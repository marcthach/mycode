#!/usr/bin/env python3
## Script to search and stop on first match
import os, fnmatch

## Define a function that stops searching on first match
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        for thisname in files:
            if fnmatch.fnmatch(thisname, name):
                result.append(os.path.join(root, thisname))
    return result


lookfor = input("What am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

#print(find(lookfor, lookwhere))
print
print(find_all(lookfor, lookwhere))


