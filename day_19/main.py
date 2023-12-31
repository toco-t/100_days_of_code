import random
from turtle import Turtle, Screen
from random import randint


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    colours = ("red", "orange", "yellow", "green", "blue", "purple")
    turtles = [Turtle(shape="turtle") for _ in range(len(colours))]
    for turtle, colour in zip(turtles, colours):
        turtle.penup()
        turtle.color(colour)
        turtle.setposition(x=-225, y=-150 + 60 * (turtles.index(turtle)))

    while True:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            x_coordinate, y_coordinate = turtle.position()
            if x_coordinate >= 250 - (40 / 2):
                print(f"Winner is {turtle.color()[0].capitalize()} turtle!!!")
                return


if __name__ == "__main__":
    main()
