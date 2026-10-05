import useful_functions as uf


screen = uf.new_screen(title="Трисекторне сонце з кільцями", width=600, height=600, bg="black")
t = uf.new_turtle(speed=0, color="blue", size=2)


def draw_trisector_sun(t):
    t.forward(120)
    t.circle(radius=15)
    t.backward(120)

    t.left(5)


for i in range(1, 73):
    if 1 <= i <= 24:
        t.color("darkgreen")
    elif 24 < i <= 48:
        t.color("olivedrab")
    elif 48 < i <= 72:
        t.color("orange")

    draw_trisector_sun(t)


t.hideturtle()
screen.exitonclick()
