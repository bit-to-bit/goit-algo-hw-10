"""Monte Carlo method"""

import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Кількість експериментів
NUM_EXPERIMENTS = 10000000


# Визначення функції та межі інтегрування
def f(x):
    """Integral function"""
    return np.sin(x) + 2


A = 0  # Нижня межа
B = 7  # Верхня межа

RECTANGLE_HEIGHT = 4  # Висота прямокутника
RECTANGLE_WIDTH = B - A  # Ширина прямокутника


def monte_carlo_simulation(A, B, rectangle_height, rectangle_width, num_experiments):
    """Area by Monte Carlo mathod"""
    inside_points = 0
    random.seed(42)
    for i in range(1, num_experiments + 1):
        point_x = random.uniform(A, B)
        point_y = random.uniform(0, rectangle_height)
        if point_y <= f(point_x):
            inside_points += 1
    # Розрахунок площі за методом Монте-Карло
    return (inside_points / num_experiments) * (rectangle_height * rectangle_width)


area_monte_carlo = monte_carlo_simulation(
    A, B, RECTANGLE_HEIGHT, RECTANGLE_WIDTH, NUM_EXPERIMENTS
)

area_scipy, error = integrate.quad(f, A, B)

s_monte_carlo = f"Площа методом Монте-Карло = {round(area_monte_carlo,4)}"
s_scipy = f"Площа бібліотекою scipy = {round(area_scipy,4)}"

print(s_monte_carlo)
print(s_scipy)

# Створення діапазону значень для x
x = np.linspace(0, 10, 600)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(A, B)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=A, color="gray", linestyle="--")
ax.axvline(x=B, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = sin(x) + 2 від " + str(A) + " до " + str(B))
ax.text(0.25, 0.75, s_monte_carlo, fontsize=12)
ax.text(0.25, 0.25, s_scipy, fontsize=12)
plt.grid()
plt.show()
