time = int(input("Введите количество секунд: "))
hour = time // 3600
rest_hour = time % 3600
minutes = rest_hour // 60
seconds = time % 60
if time < 60:
    print(time, "сек")
elif 3600 > time >= 60:
    if seconds != 0:
        print(minutes, "мин", seconds, "сек")
    else:
        print(minutes, "мин")
elif 86400 > time >= 3600:
    if rest_hour == 0:
        print(hour, "час",)
    elif minutes == 0:
        print(hour, "час", seconds, "сек")
    elif seconds == 0:
        print(hour, "час", minutes, "мин")
    else:
        print(hour, "час", minutes, "мин", seconds, "сек")
elif time >= 86400:
    day = time // 86400
    rest_day = time % 86400
    hour = rest_day // 3600
    rest_hour = rest_day % 3600
    minutes = rest_hour // 60
    seconds = rest_hour % 60
    if rest_day == 0:
        print(day, "дн")
    elif rest_day < 60:
        print(day, "дн", seconds, "сек")
    elif 3600 > rest_day >= 60:
        if seconds != 0:
            print(day, "дн", minutes, "мин", seconds, "сек")
        else:
            print(day, "дн", minutes, "мин")
    elif 86400 > rest_day >= 3600:
        if rest_hour == 0:
            print(day, "дн", hour, "час", )
        elif minutes == 0:
            print(day, "дн", hour, "час", seconds, "сек")
        elif seconds == 0:
            print(day, "дн", hour, "час", minutes, "мин")
        else:
            print(day, "дн", hour, "час", minutes, "мин", seconds, "сек")
    else:
        print(day, "дн", hour, "час", minutes, "мин", seconds, "сек")