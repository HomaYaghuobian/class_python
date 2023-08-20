from turtle import*
# setup(width=1000, height=600)
# s = Screen()
# s.title("")
# colors=['red','purple','blue','green','yellow','orange']
# bgcolor('black')
# speed("fastest")
# for x in range(321):
#     pencolor(colors[x % 6])
#     width(x/100+1)
#     forward(x)
#     left(59)
# hideturtle ()
# done()

t=Turtle()
t.shape("turtle")
t.color("blue")
t.speed("fast")
screen = Screen()
screen.title("")
t.width(3)
for i in range(8):
   for j in range(8):
      t.forward(100)
      t.right(45)
   t.right(45)
t.hideturtle()

done()