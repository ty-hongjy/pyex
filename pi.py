from math import sqrt
from random import random
from time import clock

DARTS=1200000
hits=0
clock()

for i in range(1,DARTS):
	x,y=random(),random()
	dist=sqrt(x**2+y**2)
	if dist<=1.0:
		hits=hits+1
		pi=4*(hits/DARTS)

print("Pi is %s"% pi)
print("time is %-5.5ss"% clock())
