#Способ №1
quantity = int(input("Введите количество билетов для покупки:"))

prices_ticket = 0
ticket_price_18_25 = 990
ticket_price_25 = 1390

for i in range(quantity):
    age = int(input("\nВведите возраст участника для " + str(i+1) + " билета:"))
    if age < 18:
        print("Посетители до 18 лет проходят бесплатно")
    elif 18 <= age < 25:
        print("Для посетителей от 18 до 25 стоимость билета: " + str(ticket_price_18_25))
        prices_ticket += ticket_price_18_25
    elif age >= 25:
        print("Для посетителей старше 25 стоимость билета: " + str(ticket_price_25))
        prices_ticket += ticket_price_25

if prices_ticket == 0 and quantity == 0:
    print("\nНет приобретаемых билетов")
elif prices_ticket == 0 and quantity > 0:
    print("\nВсе посетители младше 18 лет, стоимость билетов - 0 руб.")
elif quantity > 3:
    prices_ticket = prices_ticket * 0.9
    print("\nПри регистрации больше 3 посителей предоставляется скидка 10%." 
          "\nСтоимость всех билетов: " + str(prices_ticket))
else:
    print("\nСтоимость всех билетов: " + str(prices_ticket))

#Возможен ли более простой способ? Попробовала ниже. Способ №2
quantity = int(input("Введите количество билетов для покупки:"))

prices_ticket = []
ticket_price = [0, 990, 1390]
price_cond = []

for i in range(quantity):
    age = int(input("\nВведите возраст участника для " + str(i+1) + " билета:"))
    if age < 18:
        price_cond.append(ticket_price[0])
    elif 18 <= age < 25:
        price_cond.append(ticket_price[1])
    elif age >= 25:
        price_cond.append(ticket_price[2])

sum(price_cond)
if quantity > 3:
    print("Стоимость билетов:" + str(sum(price_cond)*0.9))
else:
    print("Стоимость билетов:" + str(sum(price_cond)))

