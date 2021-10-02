duration = int(input('Введите продолжительность времени в секундах: '))
result = ('Итоговое время: ')
time = {"day": duration // 86400, "hour": duration // 3600 % 24, "min": duration // 60 % 60, "sek": duration % 60}
if time["day"] > 0:
    result = result + str(time["day"]) +' дн '
if time["hour"] > 0:
    result = result + str(time["hour"]) + ' час '
if time["min"] >= 0:
    result = result + str(time["min"]) + ' мин '
if time["sek"] >= 0:

    result = result + str(time["sek"]) + ' c '
print(result)
