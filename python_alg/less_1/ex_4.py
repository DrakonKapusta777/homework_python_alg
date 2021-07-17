# 4. Написать программу, которая генерирует в указанных пользователем границах:
#      случайное целое число;
#      случайное вещественное число;
#      случайный символ.

import random

print('Укажите границы для случайного целого числа:')
x1 = int(input('x1 = '))
x2 = int(input('x2 = '))
print('Укажите границы для случайного вещественного числа:')
y1 = float(input('y1 = '))
y2 = float(input('y2 = '))
print('Укажите границы для случайного символа:')
char1 = str(input('char1 = '))
char2 = str(input('char2 = '))

r_int = random.randint(x1, x2)
r_float = random.uniform(y1, y2)
r_char = chr(random.randint(ord(char1), ord(char2)))

print(f'Случайное целое число: {r_int}\n'
      f'Случайное вещественное число: {r_float}\n'
      f'Случайный символ: "{r_char}"')
