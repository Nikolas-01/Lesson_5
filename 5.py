# 1. проверка числа на простоту.
from math import sqrt
def num_simple(n):
    if n <= 1:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
n = int(input('Введите натуральное число '))
print('1) проверяем на простоту\n', num_simple(n))
5
def num_divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result
print('2) Вывод списка делителей числа\n', num_divisors(n))
def num_max_divisor(n):
    if n == 1:
        return None
    return max(list(filter(num_simple, num_divisors(n))))
print('3) Вывод самого большого простого делителя числа\n', num_max_divisor(n))
