prices = [844.32, 1523.54, 467.17, 235.85, 614.72, 1436.4, 651.85, 1625.0, 321.81]
result = ""
for price in prices:
    result += f'{int(price):d} руб {int(round((price - int(price)) * 100)):02d} коп, '
print(result, 'изначальный список')
result = ""
prices.sort()
for price in prices:
    result += f'{int(price):d} руб {int(round((price - int(price)) * 100)):02d} коп, '
print(result, 'отсортированный по возрастанию список')
result = ""
prices_reversed = list(reversed(prices))
for price in prices_reversed:
    result += f'{int(price):d} руб {int(round((price - int(price)) * 100)):02d} коп, '
print(result, 'отсортированный по убыванию новый список')
result = ""
top_5 = prices_reversed[:5]
for price in top_5:
    result += f'{int(price):d} руб {int(round((price - int(price)) * 100)):02d} коп, '
print(result, '5 самых больших цен')



