import colorgram
from turtle import Turtle, Screen
from random import choice


def main():
    screen = Screen()
    screen.colormode(255)
    colours = [(colour.rgb.r, colour.rgb.g, colour.rgb.b)
               for colour in colorgram.extract("flumequine.jpeg", 30)]

    turtle = Turtle()
    turtle.shape("turtle")
    turtle.speed(0)

    space = 50
    for row in range(10):
        turtle.penup()
        starting_position = -1 * space * 9 / 2
        turtle.setposition(starting_position, starting_position + row * space)
        for column in range(10):
            turtle.dot(20, choice(colours))
            turtle.penup()
            turtle.forward(distance=space)

    turtle.hideturtle()

    screen.exitonclick()


if __name__ == "__main__":
    main()
