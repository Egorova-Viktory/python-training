per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("Введите сумму под проценты:"))
per_cent_list=list(per_cent.values())
deposit=[i*money/100 for i in per_cent_list]
print(deposit)

max_deposit=max(deposit)
print("Максимальная сумма, которую вы можете заработать:", max_deposit)