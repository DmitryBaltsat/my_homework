prices = [57.8, 46.51, 197, 2023.23, 11.4, 97.78, 14, 2230.2, 23.56, 179.25, 1056.78]
print(f'ID списка - {id(prices)}')

print('')

prices.sort(reverse=True)

for num in range(len(prices)):
    rubles = int(prices[num])
    kopeyky = round((prices[num] - prices[num]//1) * 100)
    prices[num] = (f'«{rubles} руб. {kopeyky:02d} коп.»')

print(prices)

new_prices = prices[::-1]
print(new_prices)

top_prices = new_prices[6::]
print(top_prices)

print('')

print(f'Тот же ID списка {id(prices)}')


