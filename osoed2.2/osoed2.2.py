# -*- coding: cp1251 -*-
import math

# Ввод аргумента x
x = input("Введите аргумент: ")
try:
    x = float(x)
except ValueError:
    print("Ошибка: Аргумент должен быть числом.")
    exit()

# Ввод признака (0 - число слагаемых, 1 - точность)
Priznak = 2
while True:
    try:
        Priznak = int(input("Введите 0 - число слагаемых или 1 - точность: "))
    except ValueError:
        print("Повторите ввод")
        continue
    else:
        if Priznak == 0 or Priznak == 1:
            break
        else:
            print("Должна быть 0 или 1")
            continue

# Инициализация переменных для вычислений
y = 0.0
p = x**2 / 8  # Первый член ряда
k = 1

if Priznak == 0:
    # Ввод числа слагаемых N
    N = input("Введите число слагаемых: ")
    try:
        N = int(N)
        if N <= 0:
            print("Ошибка: Число слагаемых должно быть положительным.")
            exit()
    except ValueError:
        print("Ошибка: Число слагаемых должно быть целым положительным числом.")
        exit()
    
    # Вычисление до заданного числа слагаемых
    for i in range(1, N + 1):
        y += p
        p *= -x**2 / ((2 * k + 2) * (2 * k + 3))
        k += 1
else:
    # Ввод точности E0
    E0 = input("Введите точность: ")
    try:
        E0 = float(E0)
        if E0 <= 0:
            print("Ошибка: Точность должна быть положительным числом.")
            exit()
    except ValueError:
        print("Ошибка: Точность должна быть положительным числом.")
        exit()
    
    # Вычисление до достижения заданной точности
    while True:
        term = p
        y += term
        if abs(term) < E0:
            break
        p *= -x**2 / ((2 * k + 2) * (2 * k + 3))
        k += 1

print(f"Приближенное значение функции Бесселя J2({x}) = {y:.5f}")