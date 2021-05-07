import turtle 
col = ('red','blue','brown','white','orange','green','purple')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(20)

for i in range(150):
    t.color(col[i%7])
    t.forward(i*2)
    t.left(59)
    t.width(3)