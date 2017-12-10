# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:52:57 2017

@author: ty-hongjy
"""

import math
from operator import mod
import time
def func(a,b,c):
  d=c
  c=0
  for n in(1,c%a,1):
      if mod(c,a)==0 and mod(d,b)==0:
        print( c+d,c/a,d/b)
        return 0
      elif(d-a)<0:
        print( "*",c+d,c/a,d/b)
        return -1
      else:
        c=c+a; d=d-a
    
 
def main():
  
  start=time.strftime('%H:%M:%S',time.localtime(time.time()))
  print("3,5")
  #for n in range(1,1000001,1):  
  for n in range(1,101,1):  
    func(3,5,n)
  print(start)
  print(time.strftime('%H:%M:%S',time.localtime(time.time())))

if __name__ == '__main__':
    main()
