# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys

# 2.2 Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def var1(num):
    even = 0
    odd = 0
    sum_size = sys.getsizeof(even) + sys.getsizeof(odd)
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
            sum_size += sys.getsizeof(int(i))
            sum_size += sys.getsizeof(even)
        else:
            odd += 1
            sum_size += sys.getsizeof(odd)
    return sum_size


def var2(num):
    even = 0
    odd = 0
    sum_size = sys.getsizeof(even) + sys.getsizeof(odd)
    for i in range(len(str(num))):
        num2 = num % 10
        sum_size += sys.getsizeof(num2)
        if num2 % 2 == 0:
            even += 1
            sum_size += sys.getsizeof(even)
        else:
            odd += 1
            sum_size += sys.getsizeof(odd)
        num //= 10
        sum_size += sys.getsizeof(num)
    return sum_size


def var3(num):
    l_even = [i for i in range(0, 9, 2)]
    sum_size = sys.getsizeof(l_even)
    l_odd = [i for i in range(1, 10, 2)]
    sum_size += sys.getsizeof(l_odd)
    even = 0
    odd = 0
    sum_size += sys.getsizeof(even)
    sum_size += sys.getsizeof(odd)
    for i in str(num):
        for l in l_even:
            sum_size += sys.getsizeof(l)
            if int(i) == l:
                sum_size += sys.getsizeof(int(i))
                even += 1
                sum_size += sys.getsizeof(even)
        for l in l_odd:
            if int(i) == l:
                sum_size += sys.getsizeof(int(i))
                odd += 1
                sum_size += sys.getsizeof(odd)
    return sum_size


# a = int(input('Введите число: '))
a = 123123123

print(var1(a), var2(a), var3(a))

# Первый вариант менее затратный, следует использовать его
