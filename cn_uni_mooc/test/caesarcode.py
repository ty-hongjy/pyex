# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:00:46 2017

@author: hongjy
"""
originString='abcdefghijklmnopqrstuvwxyz'
newString='nopqrstuvwxyzabcdefghijklm'

dict1={}
dict2={}

for i in range(0,26):
    dict1[originString[i]]=newString[i]     

for i in range(0,26):
    dict2[originString[i].upper()]=newString[i].upper()     

#print(dict1)
#print(dict2)

def coding(var):
    retString=""
    for ch in var:
        if ch in " ~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            retString=retString+ch
        else:
            if ch in dict1:
                retString=retString+dict1[ch]
            elif ch in dict2:
                retString=retString+dict2[ch]

    print(retString)            
    return retString

if __name__ == "__main__":
#    line="The Zen of Python"
    line=input()
    coding(line)
