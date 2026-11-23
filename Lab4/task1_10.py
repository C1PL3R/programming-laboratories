import useful_functions as uf


screen = uf.new_screen(title="Оптична розетка зі зсунутих квадратів", width=600, height=600, bg="black")
t = uf.new_turtle(speed=0, color="blue", size=2)

screen.colormode(255)

colors = [
    "cyan",  # Яскраво-блакитний (назва)
    "#ff007f",  # Неоновий рожевий / Magenta (HEX)
    (255, 215, 0),  # Насичене золото (RGB)
]


def draw_optical_outlet(t):
    for _ in range(1, 5):
        t.color(colors[i % len(colors)])
        t.forward(150)
        t.left(90)
    t.left(5)


for i in range(1, 73):
    draw_optical_outlet(t)


t.hideturtle()
screen.exitonclick()
