import turtle

s = turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.speed(3)
t.width(12)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color("red", "red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

# Draw the heart
heart()

# Create the zigzag break in the heart
t.pencolor("black")
t.penup()
t.goto(0, 170)
t.pendown()

for broken in range(3):
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(45)

# Display "Hope for the best"
t.penup()
t.goto(-150, -200)  # Adjust the position of the text
t.pendown()
t.color("white")
t.write("Hope for the best", font=("Arial", 24, "bold"))

turtle.done()