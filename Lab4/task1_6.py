import useful_functions as uf

screen = uf.new_screen(title="Візерунок «Кристал» із кіл", width=600, height=600, bg="black")
t = uf.new_turtle(speed=0)


def draw_crystal_pattern(t):
    t.circle(radius=30 + 5*i)
    t.left(18)


for i in range(1, 20):
    if (30 + 5*i) < 70:
        t.color("deepskyblue")
    elif 70 <= (30 + 5*i) < 110:
        t.color("royal blue")
    elif (30 + 5*i) >= 110:
        t.color("gold")

    t.pensize(2)

    draw_crystal_pattern(t=t)

t.hideturtle()
screen.exitonclick()
