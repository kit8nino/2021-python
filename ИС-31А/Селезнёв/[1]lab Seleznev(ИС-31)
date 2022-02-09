import math
import operator

#1.Словарь и функция генератор

#Словарь
dict = {
    "s": 19,
    "e(1)": 5,
    "l": 12,
    "e(2)": 5,
    "z": 26,
    "n": 14,
    "e(3)": 5,
    "v": 22
}

#Функция генератор
def x(n):
    if n == 0:
        return 1
    yield n ** 3

for i in dict:
    dict[i] = next(x(dict[i]))


print(dict)

#2 Сортировка по алфавиту + файл
dict_sorted_alphabet = sorted(dict, key=str.lower)
print(dict_sorted_alphabet)

FILE = open('spisok1.txt', 'w+')
FILE.write(str(dict_sorted_alphabet))
FILE.close()

#3 Сортировка по возрастанию + файл
dict_sorted_povozrast = sorted(dict.values(), reverse = False)
print(dict_sorted_povozrast)

FILE = open('spisok2.txt', 'w+')
FILE.write(str(dict_sorted_povozrast))
FILE.close()

#4.Списки значений до среднего и после

spisok = list(dict.values())
summa = sum(spisok)

dlina = len(dict)
average = summa // dlina

list_under_avg = []
list_upper_avg = []

for m in spisok:
    if m < average:
        list_under_avg.append(m)
    else:
        list_upper_avg .append(m)


print(list_under_avg)
print(list_upper_avg)
