print('Задание 2.2')
l = 30_000
p = 1
n = 1
for i in range(1, 50, 3):
    if p<=l and p*i<=l:
        p = p*i
    else:
        i = i-3
        print(p, i)
        break
print('Задание 2.5')
N = int(input("Введите N: "))
M = int(input("Введите M (не 0): "))

quotient = 0
remainder = N

if M == 0:
    print("Деление на ноль невозможно!")
else:
    for _ in range(N):
        if remainder >= M:
            remainder -= M
            quotient += 1
        else:
            break

    print("Частное:", quotient)
    print("Остаток:", remainder)

print('Задание 3.1')

import math

# Функция для вычисления суммы s
def compute_series_sum(x):
    s = 0
    i = 0
    term = 1  # Первое значение ряда (i=0)
    
    while abs(term) >= 0.0001:
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        s += term
        i += 1

    return s

# Основная функция, которая выполняет расчет для заданного диапазона
def main(a, b, h):
    x = a
    results = []

    while x <= b:
        s = compute_series_sum(x)
        y = math.cos(x)
        results.append((x, s, y))
        x += h

    return results

# Установка параметров
a = 0.1
b = 1.0
h = 0.01

# Выполнение расчетов
results = main(a, b, h)

# Вывод результатов
for x, s, y in results:
    print(f"x: {x:.1f}, S: {s:.6f}, y: {y:.6f}")