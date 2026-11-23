import useful_functions as uf

screen = uf.new_screen(title="Оптична квітка", width=600, height=600, bg="black")
t = uf.new_turtle(size=3, speed=0)


def draw_optical_flower(t):
    for _ in range(2):
        t.forward(100)
        t.left(60)
        t.forward(100)
        t.left(120)


for i in range(1, 27):
    draw_optical_flower(t=t)
    t.left(15)

    if 1 < i <= 12:
        t.color("cyan")
    elif 13 < i <= 26:
        t.color("orange")

t.hideturtle()
screen.exitonclick()
