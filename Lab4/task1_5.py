import useful_functions as uf

screen = uf.new_screen(title="Павутинка з шестикутників", width=600, height=600, bg="black")
t = uf.new_turtle(speed=0)
uf.jump(t=t, x=0, y=0)


def draw_gray_rays(t, color, size):
    t.color(color)
    t.pensize(size)

    for i in range(1, 7):
        t.forward(150)
        uf.jump(t=t, x=0, y=0)
        t.left(60 * i)


def draw_concentric_hexagons(t):
    for i in range(1, 8):
        if 1 <= i <= 5:
            t.color("white")
            t.pensize(1)
        elif 5 < i <= 7:
            t.color("yellow")
            t.pensize(3)

        uf.jump(t, 0, -(20 * i))
        t.circle(radius=20 * i, steps=6)


draw_gray_rays(t=t, color="gray", size=1)
draw_concentric_hexagons(t=t)

t.hideturtle()
screen.exitonclick()
