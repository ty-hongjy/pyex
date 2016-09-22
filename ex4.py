import turtle as TT
import time

#TT.speed("fastest")
TT.pensize(2)
TT.bgcolor("black")
colors=["red","yellow","purple","blue"]

TT.tracer(False)
for x in range(400):
	TT.forward(2*x)
	TT.color(colors[x%4])
	TT.left(91)

TT.tracer(True)
val = input("end:")

#time.sleep(30)
#done()
