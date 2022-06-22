number_of_tickets = int(input('Сколько билетов желаете приобрести?:\n'))

tickets_ages = []

for i in range(0, number_of_tickets):
    input_ages = int(input(f'Введите возраст посетителя №{i + 1}:\n'))
    tickets_ages.append(input_ages)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

full_price = sum(map(price, tickets_ages))

if number_of_tickets > 3:
    print('Сумма билетов со скидкой:', full_price  * 0.9, 'руб.')
else:
    price = 1
    print('Сумма билетов:', full_price, 'руб.')
