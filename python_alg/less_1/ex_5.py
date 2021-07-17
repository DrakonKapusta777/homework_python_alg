# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Ведите две буквы латинского алфавита:')
chr1 = input('char1 = ').upper()
chr2 = input('char2 = ').upper()

pos_chr1 = ord(chr1) - 64
pos_chr2 = ord(chr2) - 64
distance = abs(pos_chr1 - pos_chr2) - 1
print(f'Буква "{chr1}" {pos_chr1}-я в алфавите\n'
      f'Буква "{chr2}" {pos_chr2}-я в алфавите\n'
      f'Между буквами {distance} букв')