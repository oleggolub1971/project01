# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
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
]
lst = random.sample(my_favorite_songs, 3)
time_lst = int(int(lst[0][1]) + int(lst[1][1]) + int(lst[2][1]) + (
    lst[0][1] + lst[1][1] + lst[2][1] - int(lst[0][1]) - int(lst[1][1]) - int(lst[2][1]))*100 // 60) # time_lst - суммарное количество минут

time_lst_sek = int(((lst[0][1] + lst[1][1] + lst[2][1] - int(lst[0][1]) - int(lst[1][1]) - int(lst[2][1]))*100) % 60)
# time_lst_sek - количество секунд для вывода в формате datetime в пункте D
print('Пункт А:')
print(lst) # Для более удобного контроля результата дополнительно выводится список песен
print(f'Три песни звучат {time_lst} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

dct = random.sample(list(my_favorite_songs_dict), 3)
time_dct = int(my_favorite_songs_dict[dct[0]]) + int(my_favorite_songs_dict[dct[1]]) + int(my_favorite_songs_dict[dct[2]]) + (
    my_favorite_songs_dict[dct[0]] + my_favorite_songs_dict[dct[1]] + my_favorite_songs_dict[dct[2]] - int(
    my_favorite_songs_dict[dct[0]]) - int(my_favorite_songs_dict[dct[1]]) - int(my_favorite_songs_dict[dct[2]]))*100 // 60 # time_lst - суммарное количество минут
print('Пункт B:')
print(dct) # Для более удобного контроля результата дополнительно выводится список песен 
time_dct = int(time_dct) # суммарное количество минут
time_dct_sek = int(((my_favorite_songs_dict[dct[0]] + my_favorite_songs_dict[dct[1]] + my_favorite_songs_dict[dct[2]] - int(my_favorite_songs_dict[dct[0]]) - int(my_favorite_songs_dict[dct[1]]) - int(my_favorite_songs_dict[dct[2]]))*100) % 60)
# time_dct_sek - количество секунд для вывода в формате datetime в пункте D
print(f'Три песни звучат {time_dct} минут')
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

print('Пункт C/А:')
lst2 = random.sample(my_favorite_songs, 3)
lst2 = [lst2[0][0], lst2[1][0], lst2[2][0]]
print(lst2)

print('Пункт C/B:')
dct2 = random.sample(list(my_favorite_songs_dict), 3)
print(dct2)

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
import datetime
print('Пункт D/A:')
time1 = datetime.time(1, time_lst, time_lst_sek).strftime('%M:%S')
print(f'Три песни звучат {time1}')

print('Пункт D/B:')
time2 = datetime.time(1, time_dct, time_dct_sek).strftime('%M:%S')
print(f'Три песни звучат {time2}')

# Такое решение сработает невсегда( 
# лучше использовать timedelta()
# например, для списка
from datetime import timedelta
from math import modf
from random import sample


total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
