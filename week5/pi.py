# Задача 1. Генерируем Пи: Пользуясь формулой Лейбница для вычисления числа Пи, 
# написать бесконечный генератор pigen(), возвращающий последовательно 
# 4, 4-4/3, 4-4/3+4/5, 4-4/3+4/5-4/7 …

def peace_of_pie():
    sign = 1
    denominator = 1
    series = 1
    yield 4*series
    while True:
        sign *= -1
        denominator += 2
        series = series + sign*(1/denominator)
        yield 4*series

pi = peace_of_pie()
print(next(pi))

for i in range(10000000):
    print(next(pi))



