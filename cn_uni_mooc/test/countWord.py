# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:57:30 2017

@author: hongjy
"""

#单词频率数组-作为y轴数据 
data = [] 
#单词数组-作为x轴数据 
words = [] 

#对文本的每一行计算词频的函数 
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
#    line="this is a python and Python"
    line=input()
    wordCounts = {}     
    processLine(line.lower(), wordCounts)              
    pairs = list(wordCounts.items())
    items = [[x,y]for (y,x)in pairs]      
    items.sort(reverse=True)
    print(items[0][1])         
    
if __name__ == '__main__':     
    main()
