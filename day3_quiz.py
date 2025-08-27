import turtle

pen = turtle.Turtle()

pen.pensize(2)
pen.speed(0)
pen.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=640, height=640)

SIDE_LENGTH = 20

START_POSITION_X = -150
START_POSITION_Y = 300

COLOR_MAP = ["white", "white", "white", "white", "white", "white", "black", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "black", "gray", "black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "yellow", "black", "white", "white", "white", "white", "white", "white", "black", "yellow", "black", "white", "white", "white", "white", "white", "white", "white", "black", "yellow", "gold", "gold", "black", "white", "white", "white", "white", "black", "yellow", "yellow", "black", "white", "white", "white", "white", "black", "black", "black", "yellow", "gold", "gold", "gold", "black", "white", "white", "white", "white", "black", "yellow", "gold", "black", "white", "white", "black", "black", "gray", "gray", "black", "gold", "gold", "gold", "black", "white", "white", "white", "white", "black", "yellow", "yellow", "yellow", "yellow", "black", "black", "yellow", "yellow", "gray", "black", "gold", "gold", "gold", "black", "white", "white", "white", "white", "white", "black", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "black", "black", "gold", "gold", "black", "white", "white", "white", "white", "black", "white", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "black", "white", "black", "gold", "gold", "black", "white", "white", "white", "black", "black", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "black", "white", "white", "gray", "gold", "gray", "white", "white", "white", "black", "yellow", "yellow", "yellow", "yellow", "white", "black", "yellow", "yellow", "yellow", "yellow", "gold", "black", "gray", "gold", "gray", "white", "white", "white", "white", "white", "black", "yellow", "yellow", "yellow", "black", "black", "red", "red", "yellow", "gold", "gold", "black", "gray", "gray", "white", "white", "white", "white", "white", "white", "black", "gold", "yellow", "yellow", "yellow", "yellow", "red", "gold", "gold", "gold", "gray", "gray", "black", "white", "white", "white", "white", "white", "white", "black", "yellow", "gold", "gold", "gold", "gold", "gold", "gold", "gold", "gold", "gold", "gold", "black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "yellow", "yellow", "yellow", "yellow", "yellow", "black", "yellow", "gold", "gold", "gold", "gray", "white", "white", "white", "white", "white", "white", "white", "white", "white", "gray", "gold", "yellow", "yellow", "yellow", "black", "yellow", "gold", "gold", "gray", "white", "white", "white", "white", "white", "white", "white", "white", "white", "gray", "gold"," gray", "gold", "gold", "gold", "gold", "black", "gold", "gold", "gold", "gray", "white", "white", "white", "white", "white", "white", "white", "white", "gray", "gray", "gray", "gray", "gray", "gold", "gold", "gold", "gold", "gold", "gray", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "gray", "gray", "gold", "gray", "gray", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "gray", "yellow", "yellow", "gray", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "gray", "gray", "gray", "white", "white", "white", "white", "white", "white", "white", ]

pen.penup()


# function for creating a pixel
def pixel(fill_color, x_value, y_value):
    pen.goto(x_value, y_value)
    pen.pendown()
    pen.color(fill_color)
    pen.fillcolor(fill_color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(SIDE_LENGTH)
        pen.right(90) 
    pen.end_fill()
    pen.penup()

number = 0
for i in range(20):
    x = START_POSITION_X
    y = START_POSITION_Y - i * 20
    for j in range(20):
        x = START_POSITION_X + j * 20
        pixel(COLOR_MAP[number], x, y)
        number += 1












turtle.done()      

for y in range(3):
    for x in range(3):
        print(f"y: {y}, x: {x}")