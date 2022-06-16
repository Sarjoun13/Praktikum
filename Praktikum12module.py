per_cent = {'ТКБ' : 5.6, 'СКБ' : 5.9, 'ВТБ' : 4.28, 'СБЕР' : 4.0}
money = int(input('Введите сумму:'))
money = money / 100 #делим на 100 , чтобы посчитать проценты
deposit = []
deposit.append((per_cent['ТКБ']) * money)
deposit.append((per_cent['СКБ']) * money)
deposit.append((per_cent['ВТБ']) * money)
deposit.append((per_cent['СБЕР']) * money)
deposit = list(map(int, deposit))
print(deposit)
max_money = max(deposit)
print('Максимальная сумма, которую вы можете заработать —', max_money)
