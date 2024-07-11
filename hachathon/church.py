from turtle import *

width(5)
speed(100)
color("goldenrod")


# drawing a square
begin_fill()
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
end_fill()

right(90)

# drawing a square N2

begin_fill()
forward(100)
right(90)
forward(170)
right(90)
forward(100)
end_fill()


begin_fill()
forward(350)
right(90)
forward(170)
right(90)
forward(100)
end_fill()

right(90)
forward(250)
left(45)
color("brown")

# drawing a roof
begin_fill()
forward(180)
left(90)
forward(180)
left(135)
forward(250)
end_fill()

color("goldenrod")
right(90)
forward(250)
right(90)
forward(70)

# drawing a door

color("chocolate")
begin_fill()
right(90)
forward(135)
left(90)
forward(110)
left(90)
forward(135)
left(90)
forward(110)
end_fill()


color("goldenrod")

forward(110)
color("darkkhaki")

# drawing a window
begin_fill()
left(90)
forward(145)
right(90)
forward(35)
right(90)
forward(145)
right(90)
forward(35)
end_fill()

forward(320)

# drawing a window 2
begin_fill()
right(90)
forward(145)
left(90)
forward(35)
left(90)
forward(145)
left(90)
forward(35)
end_fill()

exitonclick()