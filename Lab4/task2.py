import math
import turtle
from datetime import datetime

import useful_functions as uf

R = 250
R_HOUR_CLOCK_HAND = 150
R_MINUTES_CLOCK_HAND = 170
R_SECONDS_CLOCK_HAND = 200
PHI = math.pi / 2

ALPHA = math.radians(6)
ALPHA_HOUR = math.radians(30)

clock_mode = "analog"
is_date = False

# (bgcolor, dial, hour_hand, min_hand, sec_hand, zero_sec_color)
analog_theme: list[tuple[str, str, str, str, str, str]] = [
    ("white", "black", "black", "black", "red", "yellow"), # Світла
    ("black", "white", "white", "white", "red", "darkgreen"), # Темна
    ("#0B192C", "white", "#E1F7F5", "#E1F7F5", "#FF6500", "red"), # Cyberpunk
]

# (bgcolor, text_color, zero_sec_color)
digital_theme: list[tuple[str, str, str]] = [
    ("black", "lime", "yellow"),       # Темна
    ("white", "lime", "darkblue"),    # Світла
    ("#1A1A2E", "#E94560", "darkred"),   # Neon Red
]

count_analog_theme: int = 0
count_digital_theme: int = 0

days_ukr = (
    "Понеділок",
    "Вівторок",
    "Середа",
    "Четвер",
    "П'ятниця",
    "Субота",
    "Неділя",
)

screen = uf.new_screen(title="Аналоговий Годинник", width=600, height=600)
screen.tracer(0)

dial: turtle.Turtle = uf.new_turtle(speed=0)
dial.hideturtle()
dial.pensize(2)

hour_clock_hand: turtle.Turtle = uf.new_turtle(speed=0)
hour_clock_hand.hideturtle()
hour_clock_hand.pensize(6)

minutes_clock_hand: turtle.Turtle = uf.new_turtle(speed=0)
minutes_clock_hand.hideturtle()
minutes_clock_hand.pensize(2)

seconds_clock_hand: turtle.Turtle = uf.new_turtle(speed=0)
seconds_clock_hand.hideturtle()
seconds_clock_hand.pensize(2)

digital_dial = turtle.Turtle()
digital_dial.hideturtle()


def draw_dial() -> None:
    """Малює циферблат аналогового годинника."""
    dial.clear()
    for n in range(60):
        y = int(R * math.sin(PHI - n * ALPHA))
        x = int(R * math.cos(PHI - n * ALPHA))
        uf.jump(dial, x, y)
        if n % 5 == 0:
            dial.dot(10)
        else:
            dial.dot(5)


def calculate_hand_coordinates(radius: int, angle: float) -> tuple[int, int]:
    """Обчислює декартові координати кінця стрілки."""
    x = int(radius * math.cos(PHI - angle))
    y = int(radius * math.sin(PHI - angle))
    return x, y


def draw_analog_clock(now: datetime) -> None:
    """Малює аналоговий годинник."""
    global count_analog_theme, analog_theme

    bgcolor, zero_sec_color = set_analog_theme(count_analog_theme, analog_theme)
    draw_dial()

    hour: float = float(now.hour)
    minutes: int = now.minute
    seconds: int = now.second

    hour_clock_hand.clear()
    minutes_clock_hand.clear()
    seconds_clock_hand.clear()

    hour_clock_hand.goto(0, 0)

    hour = (hour % 12) + minutes / 60

    x_hour_clock_hand, y_hour_clock_hand = calculate_hand_coordinates(
        radius=R_HOUR_CLOCK_HAND, angle=hour * ALPHA_HOUR
    )

    x_minutes_clock_hand, y_minutes_clock_hand = calculate_hand_coordinates(
        radius=R_MINUTES_CLOCK_HAND, angle=minutes * ALPHA
    )

    x_seconds_clock_hand, y_seconds_clock_hand = calculate_hand_coordinates(
        radius=R_SECONDS_CLOCK_HAND, angle=seconds * ALPHA
    )

    uf.jump(hour_clock_hand, 0, 0)
    uf.jump(minutes_clock_hand, 0, 0)
    uf.jump(seconds_clock_hand, 0, 0)

    hour_clock_hand.goto(x_hour_clock_hand, y_hour_clock_hand)
    minutes_clock_hand.goto(x_minutes_clock_hand, y_minutes_clock_hand)
    seconds_clock_hand.goto(x_seconds_clock_hand, y_seconds_clock_hand)

    screen.title("Аналоговий годинник")

    if seconds == 0:
        screen.bgcolor(zero_sec_color)
        screen.bgcolor(bgcolor)


def clear_all_displays() -> None:
    """Очищає всі елементи перед зміною режиму або перемалюванням."""
    dial.clear()
    hour_clock_hand.clear()
    minutes_clock_hand.clear()
    seconds_clock_hand.clear()
    digital_dial.clear()


def draw_digital_clock(now: datetime) -> None:
    global count_digital_theme, digital_theme

    bgcolor, zero_sec_color = set_digital_theme(count_digital_theme, digital_theme)

    hour: int = now.hour
    minutes: int = now.minute
    seconds: int = now.second

    uf.jump(digital_dial, 0, -25)
    digital_dial.write(f"{hour:02d}:{minutes:02d}:{seconds:02d}",
                       align="center",
                       font=("Digital-7", 54, "normal"))

    screen.title("Цифровий годинник")

    if seconds == 0:
        screen.bgcolor(zero_sec_color)
        screen.bgcolor(bgcolor)
    if is_date:
        draw_date()


def update_clock() -> None:
    """Головний цикл оновлення (викликається через ontimer)."""
    now = datetime.now().astimezone()

    if clock_mode == "analog":
        digital_dial.clear()
        draw_analog_clock(now)
    else:
        dial.clear()
        hour_clock_hand.clear()
        minutes_clock_hand.clear()
        seconds_clock_hand.clear()
        draw_digital_clock(now)

    screen.update()
    screen.ontimer(update_clock, 200)


def draw_date():
    global clock_mode, is_date

    if clock_mode == "digital":
        now = datetime.now()

        year: int = now.year
        month: int = now.month
        day: int = now.day
        day_name: str = days_ukr[now.weekday()]

        uf.jump(digital_dial, 0, -100)
        digital_dial.write(f"{day:02d}.{month:02d}.{year} | {day_name}",
                           align="center",
                           font=("Digital-7", 45, "normal"))
        is_date = False

    if is_date:
        is_date = False
    else:
        is_date = True


def set_mode(x: float = 0.0, y: float = 0.0) -> None:
    global clock_mode, is_date
    if clock_mode == "analog":
        clock_mode = "digital"
    else:
        clock_mode = "analog"
        is_date = False


def set_date(x: float = 0.0, y: float = 0.0):
    global is_date
    if is_date is False:
        is_date = True
    else:
        is_date = False


def set_analog_theme(count:int, theme_list: list):
    bgcolor, dial_color, hour_hand_color, min_hand_color, sec_hand_color, zero_sec_color = theme_list[count]

    screen.bgcolor(bgcolor)
    dial.color(dial_color)
    hour_clock_hand.color(hour_hand_color)
    minutes_clock_hand.color(min_hand_color)
    seconds_clock_hand.color(sec_hand_color)

    return bgcolor, zero_sec_color


def set_digital_theme(count:int, theme_list: list):
    bgcolor, text_color, zero_sec_color = theme_list[count]

    digital_dial.clear()

    screen.bgcolor(bgcolor)
    digital_dial.color(text_color)

    return bgcolor, zero_sec_color


def next_theme():
    global count_analog_theme, count_digital_theme, clock_mode

    if clock_mode == "analog":
        count_analog_theme = (count_analog_theme + 1) % len(analog_theme)
        set_analog_theme(count_analog_theme, analog_theme)
    else:
        count_digital_theme = (count_digital_theme + 1) % len(digital_theme)
        set_digital_theme(count_digital_theme, digital_theme)


def previuos_theme():
    global count_analog_theme, count_digital_theme, clock_mode

    if clock_mode == "analog":
        count_analog_theme = (count_analog_theme - 1) % len(analog_theme)
        set_analog_theme(count_analog_theme, analog_theme)
    else:
        count_digital_theme = (count_digital_theme - 1) % len(digital_theme)
        set_digital_theme(count_digital_theme, digital_theme)


screen.onclick(set_mode, btn=3)
screen.onclick(set_date, btn=1)

screen.onkeypress(next_theme, "Right")
screen.onkeypress(previuos_theme, "Left")

screen.onkeypress(next_theme, "Up")
screen.onkeypress(previuos_theme, "Down")

screen.listen()
update_clock()
turtle.mainloop()
