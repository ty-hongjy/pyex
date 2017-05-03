# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:00:46 2017

@author: hongjy
"""

#if __name__ == "__main__":
    
line=input()
if len(line)>=2:
    if line[-2:]=="PY":
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    

#if line[-2:]=="PY":
#    print("YES")
#else:
#    print("NO")
