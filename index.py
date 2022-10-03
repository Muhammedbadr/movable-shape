from turtle import *
colors=['blue','purple','red','green','yellow','orange','bright']


bgcolor(black)
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    right(59)
    speed(100)