# -*- coding: cp1251 -*-
import math

# ���� ��������� x
x = input("������� ��������: ")
try:
    x = float(x)
except ValueError:
    print("������: �������� ������ ���� ������.")
    exit()

# ���� �������� (0 - ����� ���������, 1 - ��������)
Priznak = 2
while True:
    try:
        Priznak = int(input("������� 0 - ����� ��������� ��� 1 - ��������: "))
    except ValueError:
        print("��������� ����")
        continue
    else:
        if Priznak == 0 or Priznak == 1:
            break
        else:
            print("������ ���� 0 ��� 1")
            continue

# ������������� ���������� ��� ����������
y = 0.0
p = x**2 / 8  # ������ ���� ����
k = 1

if Priznak == 0:
    # ���� ����� ��������� N
    N = input("������� ����� ���������: ")
    try:
        N = int(N)
        if N <= 0:
            print("������: ����� ��������� ������ ���� �������������.")
            exit()
    except ValueError:
        print("������: ����� ��������� ������ ���� ����� ������������� ������.")
        exit()
    
    # ���������� �� ��������� ����� ���������
    for i in range(1, N + 1):
        y += p
        p *= -x**2 / ((2 * k + 2) * (2 * k + 3))
        k += 1
else:
    # ���� �������� E0
    E0 = input("������� ��������: ")
    try:
        E0 = float(E0)
        if E0 <= 0:
            print("������: �������� ������ ���� ������������� ������.")
            exit()
    except ValueError:
        print("������: �������� ������ ���� ������������� ������.")
        exit()
    
    # ���������� �� ���������� �������� ��������
    while True:
        term = p
        y += term
        if abs(term) < E0:
            break
        p *= -x**2 / ((2 * k + 2) * (2 * k + 3))
        k += 1

print(f"������������ �������� ������� ������� J2({x}) = {y:.5f}")