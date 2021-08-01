# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

import collections as cl

while True:
    try:
        n = int(input('Укажите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = cl.defaultdict()
profit_companies = cl.deque()
unprofit_companies = cl.deque()
all_sum_profit = 0


for i in range(n):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= 4:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_sum_profit += profit

all_mid_profit = all_sum_profit / n

for i, item in companies.items():
    if item >= all_mid_profit:
        profit_companies.append(i)
    else:
        unprofit_companies.append(i)
print(f'\nСредняя прибыль всех компаний составила: {all_mid_profit}')
print(f'\nПрибыль выше среднего у {len(profit_companies)} компаний:')

for name in profit_companies:
    print(name)
print(f'\nПрибыль ниже среднего у {len(unprofit_companies)} компаний:')
for name in unprofit_companies:
    print(name)

