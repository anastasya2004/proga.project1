'''
Title
Group:
Makeeva Angelina 68%
Kareva Alena 90%
Osokina Anastasya  85%
'''

import turtle
import random
wn = turtle.Screen()
wn.setup(800, 800, 0, 0)
wn.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def square (x, y, a, d):
    ''' Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param d: color
:return: None'''
    t.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor (d)
    turtle.color(d)
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()


def parallelogram(x, y, a, c, k, d):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: long side of a parallelogram
    :param c: short side of a parallelogram
    :param k: angle of rotation
    :param d: color
    :return: None'''


    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor (d)
    turtle.color(d)
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(k)
    turtle.forward(c)
    turtle.right(180-k)
    turtle.forward(a)
    turtle.right(k)
    turtle.forward(c)
    turtle.end_fill()

def triangle (x, y, a, b, c):
    '''
    Function, drawing triangle.
    :param x: right angle coordinate x
    :param y: right angle coordinate y
    :param a: leg of a triangle
    :param b: hypotenuse of triangle
    :param c: color of triangle
    :return: None'''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor ('white')
    turtle.color(c)
    turtle.speed(100)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.end_fill()
    turtle.up()


def main_pictures_Alena():
    def draw_star(size, color):
        t.color(color)
        t.begin_fill()
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()
    for i in range(100):
          x = random.randint(-600, 600)
          y = random.randint(-450, 450)
          size = random.randint(5, 20)
          color = random.choice(['white', 'yellow', 'blue', 'red'])
          t.penup()
          t.goto(x, y)
          t.pendown()
          draw_star(size, color)
    t.penup()
    t.goto(-200, 120)
    t.color('orange')
    t.begin_fill()
    t.circle(110)
    t.end_fill()

    t.penup()
    t.goto(wn.window_width() / 2, wn.window_height() / -1.6)
    t.pendown()
    t.begin_fill()
    t.color('gray')
    t.left(90)
    t.circle(400, 180)
    t.end_fill()

    t.color('light gray')
    t.penup()
    t.goto(160, -340)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.goto(-330, -330)
    t.pendown()
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.penup()
    t.goto(-100, -280)
    t.pendown()
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.penup()
    t.goto(90, -230)
    t.pendown()
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.penup()
    t.goto(-240, -220)
    t.pendown()
    t.begin_fill()
    t.circle(60)
    t.end_fill()
main_pictures_Alena()





def main_pictures_Nastya():
    t.color('yellow')
    t.penup()
    t.goto(80, -300)
    t.begin_fill()
    t.left(90)
    t.forward(20)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.end_fill()

    t.penup()
    t.goto(160, -300)
    t.begin_fill()
    t.left(120)
    t.forward(20)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.end_fill()

    t.penup()
    t.goto(240, -300)
    t.begin_fill()
    t.left(120)
    t.forward(20)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.end_fill()

    t.color('orange')
    t.penup()
    t.goto(0, -280)
    t.begin_fill()
    t.left(120)
    t.forward(300)
    t.left(120)
    t.forward(300)
    t.left(120)
    t.forward(300)
    t.end_fill()

    t.color('yellow')
    t.penup()
    t.goto(110, -150)
    t.begin_fill()
    t.left(120)
    t.forward(80)
    t.left(120)
    t.forward(80)
    t.left(120)
    t.forward(80)
    t.end_fill()

    t.penup()
    t.goto(5, -170)
    t.begin_fill()
    t.left(60)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.end_fill()

    t.penup()
    t.goto(235, -170)
    t.begin_fill()
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.end_fill()

    t.penup()
    t.goto(40, -170)
    t.begin_fill()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(220)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(220)
    t.end_fill()

    t.color('red')
    t.penup()
    t.goto(90, -300)
    t.begin_fill()
    t.left(0)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.goto(150, -335)
    t.begin_fill()
    t.left(0)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.goto(210, -300)
    t.begin_fill()
    t.left(0)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.end_fill()

    t.color('orange')
    t.penup()
    t.goto(80, -300)
    t.begin_fill()
    t.left(0)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.end_fill()

    t.penup()
    t.goto(150, -317)
    t.begin_fill()
    t.left(0)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.end_fill()

    t.penup()
    t.goto(220, -300)
    t.begin_fill()
    t.left(0)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.end_fill()

    t.color('white')
    t.penup()
    t.goto(-60, 70)
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.width(5)
    t.goto(-35, 50)
    t.pendown()
    t.left(110)
    t.forward(100)

    t.penup()
    t.width(5)
    t.goto(-95, 30)
    t.pendown()
    t.left(0)
    t.forward(100)

    t.penup()
    t.width(5)
    t.goto(-65, 50)
    t.pendown()
    t.left(0)
    t.forward(120)

main_pictures_Nastya()


def main_pictures_Gelya():
    turtle.left(-45)
    parallelogram(140, 280, 150, 80, 90, 'red')
    turtle.left(-45)
    triangle(220, 200, 80, 60, 'red')
    triangle(158, 66, 80, 60, 'red')
    turtle.left(45)
    triangle(160, 288, 120, 80, 'red')
    t.pendown()

    t.penup()
    t.goto(150, 182)
    t.color('grey')
    t.begin_fill()
    t.circle(27)
    t.end_fill()
    t.penup()
    t.goto(106, 230)
    t.color('grey')
    t.begin_fill()
    t.circle(27)
    t.end_fill()
    t.penup()
    t.goto(153, 183)
    t.color('yellow')
    t.begin_fill()
    t.circle(23)
    t.end_fill()
    t.penup()
    t.goto(109, 231)
    t.color('yellow')
    t.begin_fill()
    t.circle(23)
    t.end_fill()

    t.up()
    turtle.left(-45)
    square(-200, -200, 30, 'blue')
    square(-160, -200, 30, 'blue')
    square(-150, -120, 90, 'blue')
    square(-185, -100, 20, 'blue')
    square(-160, -30, 70, 'blue')
    square(-130, -155, 20, 'blue')
    square(-240, -155, 20, 'blue')
    square(-175, -50, 10, 'white')
    square(-205, -50, 10, 'white')
main_pictures_Gelya()
turtle.done()
