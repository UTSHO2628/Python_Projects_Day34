import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Eid Mubarak")

# Create turtle object
pen = turtle.Turtle()
pen.speed(3)  # Moderate speed for smooth drawing

# Function to draw a crescent moon with animation
def draw_crescent():
    pen.penup()
    pen.goto(-100, 50)
    pen.pendown()
    pen.color("gold")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()

    pen.color("black")
    pen.penup()
    pen.goto(-70, 80)
    pen.pendown()
    pen.begin_fill()
    pen.circle(80)
    pen.end_fill()

# Function to draw a star with smooth animation
def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("gold")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
        time.sleep(0.2)  # Delay for smooth effect
    pen.end_fill()

# Function to display "Eid Mubarak" with a fade-in effect
def draw_text():
    pen.penup()
    pen.goto(-150, -150)
    pen.color("white")

    # Gradually increase text visibility
    for i in range(5, 26, 5):
        pen.write("Eid Mubarak", align="left", font=("Arial", i, "bold"))
        time.sleep(0.2)
        pen.undo()

    pen.write("Eid Mubarak", align="left", font=("Arial", 24, "bold"))

# Execute the drawing functions
draw_crescent()
time.sleep(0.5)
draw_star(50, 150, 100)
time.sleep(0.5)
draw_text()

# Hide the turtle
pen.hideturtle()
screen.mainloop()
