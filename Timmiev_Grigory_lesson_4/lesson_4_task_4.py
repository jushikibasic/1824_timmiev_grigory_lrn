from utils import currency_rates

print(currency_rates("usd")[0], currency_rates("usd")[1], sep=', ')
print(currency_rates("eur")[0], currency_rates("eur")[1], sep=', ')
print(currency_rates("gbp")[0], currency_rates("gbp")[1], sep=', ')

