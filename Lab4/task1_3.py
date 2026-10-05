import useful_functions as uf

screen = uf.new_screen(title="Квадратна кольорова спіраль", width=600, height=600, bg="black")
t = uf.new_turtle(size=3, speed=0)


def draw_square_colored_spiral(t, length):
    t.forward(10 + length)
    t.left(90)


AUTUMN_FOREST = [
    "darkgreen",  # Глибокий зелений
    "olivedrab",  # Оливковий
    "darkgoldenrod",  # Темне золото
    "saddlebrown",  # Теплий коричневий
]

for i in range(1, 61):
    t.color(AUTUMN_FOREST[i % len(AUTUMN_FOREST)])
    draw_square_colored_spiral(t=t, length=((i - 1) * 4))

    if 0 < i <= 20:
        t.pensize(2)
    elif 21 < i <= 40:
        t.pensize(3)
    elif 41 < i <= 60:
        t.pensize(4)

t.hideturtle()
screen.exitonclick()
