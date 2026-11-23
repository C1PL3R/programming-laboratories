import turtle


def new_screen(title="Turtle",
               width=700,
               height=600,
               bg="white") -> turtle._Screen:
    """Готує чисте вікно для малювання. Можна викликати скільки завгодно раз"""
    
    turtle.TurtleScreen._RUNNING = True # type: ignore[attr-defined]
    screen = turtle.Screen()
    screen.clear()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(bg)
    screen.tracer(1)
    return screen

def new_turtle(color="black",
               size=2,
               speed=6,
               shape="turtle") -> turtle.Turtle:
    """Створює черепашку із заданими налаштуваннями."""
    t = turtle.Turtle(shape=shape)
    t.color(color)
    t.pensize(size)
    t.speed(speed)
    return t

def jump(t: turtle.Turtle,
    x: float,
    y: float,
    heading: float = 0) -> None:
    """Переносить черепашку в точку (x, y) без малювання і задає напрямок."""
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
