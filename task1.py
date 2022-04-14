# Задача 1
# Приведен плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания любых трех песен в формате
# Три песни звучат XXX минут
# Сделайте необходимые вычисления заранее, а затем выводите print()

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
    ['Clocks', 5.07],
    ['Maybe Tomorrow', 4.32],
    ['Music Sounds Better With You', 6.43],
    ['Believer', 3.24],
    ['Start Me Up', 4.04]
]

from random import sample
from datetime import datetime, timedelta

fav_songs_times = [timedelta(minutes=y.minute,seconds=y.second) for y in [datetime.strptime("{0:.2f}".format(x[1]),"%M.%S") for x in sample(my_favorite_songs,3)]]
tSec = sum(fav_songs_times,timedelta()).seconds
result = "{0}.{1:02d}".format(tSec // 60, tSec % 60)
print(f"Три песни звучат {result} минут")


