"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input('Введите число n = ')
sum_elements = 0
n_power = n
for i in range(3):
	sum_elements += int(n_power)
	n_power += n
print(f'n + nn + nnn = {sum_elements}')
