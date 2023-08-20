from turtle import*
# import turtle
bgcolor('black')
a = Screen()
turtle =Turtle()
turtle.color('yellow')
turtle.speed(0)
turtle.hideturtle()
for i in range(120):
    turtle.circle(i*2)
    turtle._rotate(5)

done()