import matplotlib.pyplot as plt


def calculate_s(m1, m2, L, v):
    x1 = L / 2
    x2 = L

    v1 = -v
    v2 = 0.0

    s1 = 0.0
    count_of_collisions = 0

    max_collisions = 100000

    for _ in range(max_collisions):
        events = []

        if v1 < 0:
            t_wall = -x1 / v1
            events.append((t_wall, "wall"))

        if v1 > v2:
            t_ball = (x2 - x1) / (v1 - v2)
            events.append((t_ball, "ball"))

        if not events:
            break

        t, event = min(events, key=lambda item: item[0])

        s1 += abs(v1) * t

        x1 += v1 * t
        x2 += v2 * t

        count_of_collisions += 1

        if event == "wall":
            v1 = -v1

        elif event == "ball":
            u1 = (
                (m1 - m2) / (m1 + m2) * v1
                + (2 * m2) / (m1 + m2) * v2
            )

            u2 = (
                (2 * m1) / (m1 + m2) * v1
                + (m2 - m1) / (m1 + m2) * v2
            )

            v1, v2 = u1, u2

    return s1, count_of_collisions


m1 = 5
m2 = 500
L = 300
v = 120


m1_list = list(range(2, 102, 5))
s1_list = []

for mass in m1_list:
    s, _ = calculate_s(mass, m2, L, v)
    s1_list.append(s)

plt.figure(figsize=(8, 5))
plt.plot(m1_list, s1_list, marker="o", label="S(m)")
plt.title("Залежність шляху від маси малої кульки")
plt.xlabel("Маса малої кульки m")
plt.ylabel("Повний шлях S")
plt.grid(True)
plt.legend()
plt.tight_layout()


m2_list = list(range(5, 105, 5))
s2_list = []

for mass in m2_list:
    s, count_of_collisions = calculate_s(m1, mass, L, v)
    s2_list.append(s)

plt.figure(figsize=(8, 5))
plt.plot(m2_list, s2_list, marker="s", label="S(M)")
plt.title("Залежність шляху від маси великої кульки")
plt.xlabel("Маса великої кульки M")
plt.ylabel("Повний шлях S")
plt.grid(True)
plt.legend()
plt.tight_layout()


L_list = list(range(100, 501, 20))
s_L_list = []

for distance in L_list:
    s, count_of_collisions = calculate_s(m1, m2, distance, v)
    s_L_list.append(s)

plt.figure(figsize=(8, 5))
plt.plot(L_list, s_L_list, marker="^", label="S(L)")
plt.title("Залежність шляху від відстані до великої кульки")
plt.xlabel("Початкова відстань L")
plt.ylabel("Повний шлях S")
plt.grid(True)
plt.legend()
plt.tight_layout()


v_list = list(range(100, 1100, 50))
s_v_list = []

for speed in v_list:
    s, count_of_collisions = calculate_s(m1, m2, L, speed)
    s_v_list.append(s)

plt.figure(figsize=(8, 5))
plt.plot(v_list, s_v_list, marker="d", label="S(v)")
plt.title("Залежність шляху від початкової швидкості")
plt.xlabel("Початкова швидкість v")
plt.ylabel("Повний шлях S")
plt.grid(True)
plt.legend()
plt.tight_layout()


ratio_list = [
    10 ** (-2 + i * 4 / 99)
    for i in range(100)
]

collision_counts = []

for ratio in ratio_list:
    small_mass = ratio
    large_mass = 1.0

    s, count = calculate_s(small_mass, large_mass, L, v)
    collision_counts.append(count)

plt.figure(figsize=(8, 5))
plt.plot(ratio_list, collision_counts, label="N(m/M)")
plt.xscale("log")
plt.title("Залежність кількості зіткнень від співвідношення мас")
plt.xlabel("Співвідношення мас m/M")
plt.ylabel("Кількість зіткнень N")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
