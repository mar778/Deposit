money = int(input("Введите сумму, которую вы хотите поместить под проценты:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(per_cent[key] * money / 100)
deposit_max = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать:", deposit_max)
