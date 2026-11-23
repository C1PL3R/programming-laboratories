import useful_functions as uf

screen = uf.new_screen(title="Візерунок «Кристал» із кіл", width=600, height=600, bg="black")
t = uf.new_turtle(speed=0)


def draw_colored_hexagonal_spiral(t, x):
    t.forward(x)
    t.left(59)


AUTUMN_FOREST = [
    "darkgreen",    # Глибокий зелений
    "olivedrab",    # Оливковий
    "darkgoldenrod",# Темне золото
    "saddlebrown",  # Теплий коричневий
    "firebrick",    # Цегляно-червоний
    "orange"        # Яскравий оранжевий
]

for i in range(1, 361):
    t.color(AUTUMN_FOREST[i % len(AUTUMN_FOREST)])
    t.pensize((i/100) + 1)
    draw_colored_hexagonal_spiral(t=t, x=i)

t.hideturtle()
screen.exitonclick()
