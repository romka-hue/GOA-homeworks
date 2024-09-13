from turtle import *


speed(30)
width(9)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
left(90)
#door
begin_fill()
color("brown")
forward(120)
right(90)

forward(60)
right(90)
forward(120)
end_fill()

#end of door

penup()
goto(200, 200)
pendown()
begin_fill()
color("green")
right(150)
forward(200)
left(120)
forward(200)
end_fill() 
#end
#buildig a windows "left"
penup()
goto(10,60)
pendown()
left(30)
#end

color("blue")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

end_fill()
#end
#right window
begin_fill()
penup()
goto(140,60)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#handle of door 
begin_fill()
color("yellow")
penup()
goto(120, 60)
pendown()
circle(5)
end_fill()

#just some setting
exitonclick()
hideturtle()
