from turtle import *


#we want to paint a house
#step 1: draw a square
speed(40)
width(6)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door


forward(70)
color("green")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
color("blue")
goto(180,180)
color("yellow")
begin_fill()
left(30)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(180)
forward(45)
end_fill()
color("blue")
forward(77)
color("yellow")
begin_fill()
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()

left(90)
forward(22)
left(90)
color("brown")
forward(45)
color("yellow")
right(90)
forward(22)
right(90)
forward(22)
right(90)
color("brown")
forward(45)
color("blue")
forward(77)
color("brown")
forward(45)
left(90)
color("yellow")
forward(22)
left(90)
forward(22)
left(90)
color("brown")
forward(45)

exitonclick()