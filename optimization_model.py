import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")  # Кількість лимонаду
juice = pulp.LpVariable("Juice", lowBound=0, cat="Integer")  # Кількість соку

# Функція цілі (Максимізація прибутку)
model += lemonade + juice, "Production"

# Додавання обмежень
model += 2 * lemonade + 1 * juice <= 100  # Обмеження: вода
model += 1 * lemonade + 0 * juice <= 50  # Обмеження: цукор
model += 1 * lemonade + 0 * juice <= 30  # Обмеження: лимонний сік
model += 0 * lemonade + 2 * juice <= 40  # Обмеження: фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Виробляти лимонаду: {lemonade.varValue}")
print(f"Виробляти фруктового соку: {juice.varValue}")
print(f"У підсумку максимальне виробництво разом: {lemonade.varValue + juice.varValue}")
