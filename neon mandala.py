import turtle


screen=turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")


t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()

colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink"]

for i in range(80):
    t.color(colors[i % len(colors)])
    t.width(2)
    t.forward(i * 2)
    t.right(91)

t.penup()
t.goto(0, -60)
t.setheading(90)
t.pendown()
t.color("gold", "yellow")
t.begin_fill()
for i in range(5):
    t.forward(130)
    t.right(144)
t.end_fill()  

t.penup()
t.goto(0, 0)
t.pendown()  
petal_colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink"]
for i in range(36):
    t.color(petal_colors[i % len(petal_colors)],
    petal_colors[(i + 2)% len(petal_colors)])
    t.begin_fill()
    for j in range(4):
        t.forward(55)
        t.right(90)
    t.end_fill()
    t.right(10)

turtle.done()
