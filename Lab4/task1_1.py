import math
import useful_functions as uf


screen = uf.new_screen(title="Семикутна зірка", width=600, height=600)
t = uf.new_turtle(size=3, speed=0)


def draw_star(t, cx: int, cy: int, n: int, k: int, R:int):
    """Зірка {n/k} з центром (cx, cy) і радіусом R."""
    side = 2 * R * math.sin(math.pi * k / n)  # довжина хорди
    uf.jump(t=t, x=cx, y=cy - R, heading=180 * k / n)
    t.left(25)
    for _ in range(n):
        t.forward(side)
        t.left(360 * k / n)


stars = [
    (0, 0, 7, 2, 125, "gold")
]

for cx, cy, n, k, R, color in stars:
    t.begin_fill()

    t.color("blue", color)
    draw_star(t, cx, cy, n, k, R)
    uf.jump(t, cx, cy)

    t.end_fill()

t.hideturtle()
screen.exitonclick()
