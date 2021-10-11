# Задача 2. Итерируемся: Написать функцию chainslice(begin, end, seq0, seq1, …), 
# которая принимает не менее трёх параметров: два целых числа и не менее одной последовательности. 
# Рассмотрим последовательность seq, образованную всеми элементами seq0, затем — всеми элементами seq1, и т. д. 
# Вернуть эта функция должна итератор, пробегающий элементы последовательности seq с begin до end - 1 включительно.

from itertools import chain, islice

def chainslice(begin, end, *seqs):

    seq_iterator = chain(*seqs)

    return islice(seq_iterator, begin, end, None)

it = chainslice(2, 10, ['zero', 1, 'two'], [3, 4, 'five', 6], 'seven')

print(list(it))




