import math
import time

import useful_functions as uf


m1 = 5
m2 = 500

v1 = -50.0
v2 = 0.0

r_lighter = 20
r_heavier = 40

left_wall = -300
right_wall = 300

x1 = -75.0
x2 = 0.0

count_of_touch = 0

screen = uf.new_screen(title="Зіткнення кульок", width=600, height=600,)
screen.bgcolor("black")
screen.tracer(0)

lighter_ball = uf.new_turtle(speed=0, color="red", shape="circle")
heavier_ball = uf.new_turtle(speed=0, color="green", shape="circle")

lighter_ball.penup()
heavier_ball.penup()

lighter_ball.shapesize(stretch_wid=r_lighter / 10, stretch_len=r_lighter / 10)
heavier_ball.shapesize(stretch_wid=r_heavier / 10, stretch_len=r_heavier / 10)

lighter_ball.goto(x1, -290 + r_lighter)
heavier_ball.goto(x2, -290 + r_heavier)

screen.update()


def animate_move(dt: float) -> None:
    global x1, x2

    start_x1 = x1
    start_x2 = x2

    distance = max(abs(v1 * dt), abs(v2 * dt))
    frames = max(1, math.ceil(distance / 4))

    for frame in range(1, frames + 1):
        fraction = frame / frames

        lighter_ball.setx(start_x1 + v1 * dt * fraction)
        heavier_ball.setx(start_x2 + v2 * dt * fraction)

        screen.update()
        time.sleep(0.01)

    x1 = start_x1 + v1 * dt
    x2 = start_x2 + v2 * dt


while True:
    events = []

    wall_x = left_wall + r_lighter

    if v1 < 0:
        dt_wall = (wall_x - x1) / v1
        if dt_wall >= 0:
            events.append((dt_wall, "wall"))

    contact_distance = r_lighter + r_heavier
    gap = x2 - x1 - contact_distance
    relative_velocity = v1 - v2

    if gap >= 0 and relative_velocity > 0:
        dt_ball = gap / relative_velocity
        events.append((dt_ball, "ball"))

    exit_x = right_wall + r_heavier

    if v2 > 0:
        dt_exit = (exit_x - x2) / v2
        if dt_exit >= 0:
            events.append((dt_exit, "exit"))

    if not events:
        break

    dt, event = min(events, key=lambda item: item[0])

    animate_move(dt)

    if event == "wall":
        v1 = -v1

    elif event == "ball":
        u1 = (((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2)

        u2 = (((2 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2)

        v1, v2 = u1, u2
        count_of_touch += 1

    elif event == "exit":
        break

screen.mainloop()
