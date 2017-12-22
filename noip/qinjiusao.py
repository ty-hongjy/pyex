# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:58:48 2017

@author: hongjy
"""

def fun(n,x):
    tmp=1
    if(n==0):
        return 1;
#    for i in range(1,n+1):
#        tmp=tmp*x
    tmp=pow(x, n)
    print("N:",n," , ",tmp)
    return tmp+fun(n-1,x)
    
def main():
    fun1=fun(5,5)
    print("5,3",fun1)
    
if __name__=="__main__":
    main()