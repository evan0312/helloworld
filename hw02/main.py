import turtle
import math

#定义将弧度转为角度的函数
def trans(rad):
    angle=180*rad/math.pi
    return angle

#设置各小星与大星中心连线和水平方向的夹角
a=trans(math.atan(3/5))
b=trans(math.atan(1/7))
c=trans(math.atan(2/7))
d=trans(math.atan(4/5))

#定义绘制旗面的函数
#输入旗面的宽度
def flag(width):
    global i #定义全局变量i,i为一个单元格的长度
    i=1.5*width/30
    turtle.color("red","red")
    turtle.penup()
    turtle.goto(-0.75*width,0.5*width)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(1.5*width)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()

#定义绘制星星的函数
#输入五角星的中心坐标、外接圆半径、起点与其中心连线的偏角
def star(center_of_star,radius,angle):
    turtle.penup()
    turtle.goto(center_of_star)
    turtle.setheading(90)#将画笔方向恢复为正北方向
    turtle.left(angle)
    turtle.fd(radius)
    turtle.right(162)
    turtle.color("yellow","yellow")
    turtle.pendown()
    l=2*radius*math.cos(math.atan(1/3))
    turtle.begin_fill()#一笔画五角星
    for _ in range(5):
        turtle.fd(l)
        turtle.right(144)
    turtle.end_fill()

turtle.speed(6)
#输入红旗的宽度
flag(300)
star((-10*i,5*i),3*i,72)
star((-5*i,8*i),i,90+a)
star((-3*i,6*i),i,90+b)
star((-3*i,3*i),i,90-c)
star((-5*i,i),i,90-d)
turtle.hideturtle()
