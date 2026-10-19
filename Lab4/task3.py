from random import randint
import time
import useful_functions as uf

m1, m2 = 5, 50

dt = 0.1

v1 = 100
v2 = -100

screen = uf.new_screen(title="Зіткнення кульок", width=600, height=600)
screen.bgcolor("black")

r_lighter = 15
r_heavier = 5 * (m2 / m1)

lighter_ball = uf.new_turtle(speed=0, color="red", shape="circle")
heavier_ball = uf.new_turtle(speed=0, color="green", shape="circle")

lighter_ball.penup()
heavier_ball.penup()

lighter_ball.goto(-randint(50, 150), -290 + r_lighter)
heavier_ball.goto(randint(50, 150), -290 + r_heavier)

lighter_ball.shapesize(stretch_wid=r_lighter / 10, stretch_len=r_lighter / 10)
heavier_ball.shapesize(stretch_wid=r_heavier / 10, stretch_len=r_heavier / 10)

has_collided = False

for frame in range(1200):
    x1 = lighter_ball.xcor() + v1 * dt
    x2 = heavier_ball.xcor() + v2 * dt

    distance = abs(x1 - x2)
    min_distance = r_lighter + r_heavier

    if distance <= min_distance and not has_collided:
        u1 = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2
        u2 = ((2 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2

        v1 = u1
        v2 = u2
        has_collided = True
    elif distance > min_distance:
        has_collided = False

    if x1 + r_lighter >= 300 and v1 > 0:
        v1 = -v1
    elif x1 - r_lighter <= -300 and v1 < 0:
        v1 = -v1

    if x2 + r_heavier >= 300 and v2 > 0:
        v2 = -v2
    elif x2 - r_heavier <= -300 and v2 < 0:
        v2 = -v2

    lighter_ball.setx(x1)
    heavier_ball.setx(x2)

    screen.update()
    time.sleep(0.01)

screen.mainloop()
