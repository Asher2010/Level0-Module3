import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    Turty = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    for i in range(6):
        Turty.forward(200)
        Turty.left(90)
        Turty.forward(200)
        Turty.left(90)
        Turty.forward(200)
        Turty.left(90)
        Turty.forward(200)
    #      3) Set the pen width to 10

        Turty.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
        Color = simpledialog.askstring(title="Color", prompt="What color pen would you like to draw with?")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
        if Color == "blue":
            Turty.pencolor("blue")
        elif Color == "red":
            Turty.pencolor("red")
        elif Color == "green":
            Turty.pencolor("green")
        else:
            Turty.pencolor(get_random_color())

    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
