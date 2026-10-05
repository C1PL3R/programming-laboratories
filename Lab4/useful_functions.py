import turtle
import random
import math
import time

def new_screen(title="Turtle", width=700, height=600, bg="white"):
    """Готує чисте вікно для малювання. Можна викликати скільки завгодно раз"""
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen()
    screen.clear()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(bg)
    screen.tracer(1)
    return screen

def new_turtle(color="black", size=2, speed=6, shape="turtle"):
    """Створює черепашку із заданими налаштуваннями."""
    t = turtle.Turtle(shape=shape)
    t.color(color)
    t.pensize(size)
    t.speed(speed)
    return t

def jump(t: object, x: object, y: object, heading: object = 0) -> None:
    """Переносить черепашку в точку (x, y) без малювання і задає напрямок."""
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
