# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:00:46 2017

@author: hongjy
"""

if __name__ == "__main__":
#    vege='西红柿, 花椰菜'
#    vege='食材1, 食材2, 食材3'
    vege=input()
    vegelist=vege.split(',')
#    print(vegelist)
#    print(len(vegelist))
    for ve in vegelist:
        for ve1 in vegelist:
            if ve1 != ve:
                print(ve,ve1)
