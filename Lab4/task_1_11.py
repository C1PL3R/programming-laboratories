import useful_functions as uf

screen = uf.new_screen(title="Пейзаж", width=600, height=600, bg="#FFDAAF")
t = uf.new_turtle(speed=0, size=2)


def draw_polygon(t, points, color):
    t.color(color)
    t.begin_fill()
    for x, y in points:
        t.goto(x, y)
    t.end_fill()


def draw_bird(t, x: float, y: float, size: float = 1.0, color="#281914"):
    r1, ext1 = 25 * size, 35
    r2, ext2 = 35 * size, 35

    uf.jump(t, x, y)
    t.color(color, color)
    t.setheading(180)

    t.begin_fill()

    t.circle(r1, ext1)
    t.left(120)
    t.circle(-r2, ext2)

    t.left(90)
    t.circle(-r2, ext2)
    t.left(120)
    t.circle(r1, ext1)

    t.end_fill()


uf.jump(t, -300, 0)
draw_polygon(t=t, points=[(-300, 150), (300, 150), (300, 0)], color="#FFDECD")

uf.jump(t, -300, -300)
draw_polygon(t=t, points=[(-300, -150), (300, -150), (300, -300)], color="#A57D8C")

t.penup()
t.goto(0, 150)
t.dot(60, "#FFF000")  # Сонце

uf.jump(t, -300, 0)
mountain_orange = [
    (-300, 0),
    (-270, 30),
    (-250, 65),
    (-230, 95),
    (-200, 105),
    (-155, 74),
    (-100, 20),
    (-70, 35),
    (-30, 70),
    (-10, 90),
    (0, 110),
    (10, 150),
    (30, 150),
    (50, 120),
    (90, 90),
    (100, 53),
    (105, 20),
    (125, 20),
    (140, 50),
    (150, 90),
    (170, 130),
    (190, 50),
    (210, 50),
    (250, 100),
    (300, 60),
    (300, 0),
]
draw_polygon(t=t, points=mountain_orange, color="#F58723")

uf.jump(t, -300, -150)
mountain_red = [
    (-300, -154),
    (-290, -106),
    (-280, -97),
    (-260, -72),
    (-240, -31),
    (-220, -5),
    (-210, 15),
    (-190, 33),
    (-180, 15),
    (-150, -26),
    (-120, -57),
    (-60, -94),
    (-30, -126),
    (-5, -87),
    (0, 0),
    (30, 80),
    (70, 100),
    (104, -20),
    (105, -25),
    (110, -50),
    (150, -100),
    (180, -80),
    (200, -60),
    (220, -40),
    (270, -30),
    (300, -150),
]
draw_polygon(t=t, points=mountain_red, color="#B9412D")

uf.jump(t, -300, -300)
mountain_violet = [
    (-300, -300),
    (-300, -100),
    (-270, -90),
    (-250, -120),
    (-230, -160),
    (-200, -180),
    (-170, -210),
    (-160, -260),
    (-140, -230),
    (-130, -200),
    (-110, -170),
    (-90, -210),
    (-50, -250),
    (-30, -300),
    (30, -300),
    (60, -250),
    (90, -220),
    (120, -170),
    (140, -120),
    (180, -60),
    (200, -60),
    (220, -80),
    (240, -120),
    (280, -180),
    (300, -220),
    (300, -300),
]
draw_polygon(t=t, points=mountain_violet, color="#2D1423")

draw_bird(t=t, x=67, y=67, size=1)
draw_bird(t=t, x=45, y=-67, size=1)
draw_bird(t=t, x=-180, y=150, size=1)
draw_bird(t=t, x=270, y=60, size=1)

draw_bird(t=t, x=-204, y=119, size=1)
draw_bird(t=t, x=-84, y=-173, size=1)
draw_bird(t=t, x=259, y=109, size=1)
draw_bird(t=t, x=-95, y=28, size=1)

t.hideturtle()
screen.exitonclick()
