# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:52:57 2017

@author: ty-hongjy
"""

import math
from operator import mod

def func(a,b,c,d):
  if mod(c,a)==0 and mod(d,b)==0:
    #print( c+d,c/a,d/b)
    return 0
  elif(d-a)<0:
    print( "*",c+d,c/a,d/b)
    return -1
  else:
    func(a,b,c+a,d-a)
    

def main():
  print("3,7")
  for n in range(11,101,1):  
    func(3,7,0,n)
  
  print("3,5")
  for n in range(1,100001,1):  
    func(3,5,0,n)

if __name__ == '__main__':
    main()
