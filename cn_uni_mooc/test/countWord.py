# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:57:30 2017

@author: hongjy
"""
from operator import itemgetter, attrgetter

def processLine(line, wordCounts):     
    line = replacePunctuations(line)     
    words = line.split()      
    for word in words:         
        if word in wordCounts:             
            wordCounts[word] += 1         
        else:             
            wordCounts[word] = 1 

def replacePunctuations(line):     
    for ch in line:         
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":             
            line = line.replace(ch, " ")     
    return line 

def main():   
    line="this is a python and Python"
#    line=input()
    wordCounts = {}     
    processLine(line.lower(), wordCounts)              
    items = sorted(list(wordCounts.items()),key=itemgetter(1),reverse=True)
#    print(items)
    print(items[0][0])

#    pairs = list(wordCounts.items())
#    items = [[x,y]for (y,x)in pairs]      
#    items.sort(reverse=True)
#    print(items)
#    print(items[0][1])         

if __name__ == '__main__':     
    main()
