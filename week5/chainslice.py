# Задача 2. Итерируемся: Написать функцию chainslice(begin, end, seq0, seq1, …), 
# которая принимает не менее трёх параметров: два целых числа и не менее одной последовательности. 
# Рассмотрим последовательность seq, образованную всеми элементами seq0, затем — всеми элементами seq1, и т. д. 
# Вернуть эта функция должна итератор, пробегающий элементы последовательности seq с begin до end - 1 включительно.

from itertools import chain

def chainslice(begin, end, *seqs):

    seq_iterator = chain(*seqs)

    for _ in range(begin, end):
        yield next(seq_iterator)

it = chainslice(1, 6, [1,2,3,4], [2,2], 'abc')

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))




