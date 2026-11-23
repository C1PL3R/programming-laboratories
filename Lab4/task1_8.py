import math
import useful_functions as uf


screen = uf.new_screen(title="Математична троянда", width=600, height=600, bg="black")
t = uf.new_turtle(speed=0, color="blue", size=2)


def draw_mathematical_rose(t, i):
    tetha = math.radians(i)
    r = 180 * math.cos(15 * tetha)

    x = r * math.cos(tetha)
    y = r * math.sin(tetha)

    if abs(r) > 100:
        t.color("cyan")
    else:
        t.color("magenta")

    if i == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)


for i in range(0, 181):
    draw_mathematical_rose(t, i)


t.hideturtle()
screen.exitonclick()
