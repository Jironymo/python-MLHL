# Задача 1. Генерируем Пи: Пользуясь формулой Лейбница для вычисления числа Пи, 
# написать бесконечный генератор pigen(), возвращающий последовательно 
# 4, 4-4/3, 4-4/3+4/5, 4-4/3+4/5-4/7 …

def pigen():
    sign = -1
    denominator = -1
    series = 0

    while True:
        sign *= -1
        denominator += 2
        series = series + sign*(4/denominator)
        yield series

pi = pigen()
print(next(pi))

for i in range(1000):
    print(next(pi))



