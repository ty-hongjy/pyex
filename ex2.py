from turtle import *
color("red","yellow")
#fillcolor("red")
begin_fill()
while True:
	forward(200)
	left(170)
#right(144)
	if abs(pos())<1:
		break
end_fill()
done()
