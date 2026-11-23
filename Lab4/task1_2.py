import useful_functions as uf

screen = uf.new_screen(title="Кольорова розета", width=600, height=600, bg="black")
t = uf.new_turtle(size=3, speed=0)

def draw_color_rosette(t, R: int):
    t.circle(R)
    t.left(10)

AUTUMN_FOREST = [
    "darkgreen",    # Глибокий зелений
    "olivedrab",    # Оливковий
    "darkgoldenrod",# Темне золото
    "saddlebrown",  # Теплий коричневий
    "firebrick",    # Цегляно-червоний
    "orange"        # Яскравий оранжевий
]

for i in range(1, 37):
    t.color(AUTUMN_FOREST[i % len(AUTUMN_FOREST)])
    draw_color_rosette(t=t, R=80)

t.hideturtle()
screen.exitonclick()
