# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы алфавита (1-26):'))
char = chr(num + 64)
print(f'Это буква "{char}"')
