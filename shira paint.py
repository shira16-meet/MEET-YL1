import turtle

#turtle.hideturtle()
turtle.speed(0)
smile=turtle.Turtle()
hi=turtle.Turtle()
red=turtle.Turtle()
green=turtle.Turtle()
shape="square"
color= "red"
def drawShape(x,y):
        global shape
        if(shape=="circle"):
            brush_1_circle(x,y)
        else:  
            brush_2_square(x,y)
def brush_1_circle(x,y):
    global color
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(100)

def brush_2_square(x,y):
    global color
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)

def change_to_circle(x,y):
    global shape
    shape = "circle"
def change_to_square(x,y):
    global shape
    shape = "square"
def change_color_to_red():
    global color
    color="red"
def change_color_to_green():
    global color
    color="green"
turtle.onscreenclick(drawShape)
smile.penup()
smile.goto(-500,300)
smile.pendown()
smile.onclick(change_to_circle)
hi.penup()
hi.goto(-400,300)
hi.pendown()
hi.onclick(change_to_square)
red.penup()
red.goto(-300,300)
red.pendown()
red.color("red")
red.onclick(change_color_to_red)
green.penup()
green.goto(-200,300)
green.pendown()
green.pencolor('green')
turtle.pencolor('green')
green.onclick(change_color_to_green)


turtle.mainloop()
