str='т и м о ш и н а'

key=str.split()

#print(key)

number=[20,10,14,16,26,10,15,1]

value=[]

for x in number:

    value.append(x**3)

#print(value)

a={k:v for k, v in zip(key,value)}

#Отсортировать по ключу в алфавитном порядке

keysort_a={k: a[k] for k in sorted(a)} 

#print('сортировка по алфавиту',keysort_a)

with open('алфавитный порядок.txt', 'w') as file1:

  for key, value in keysort_a.items():

    file1.write(f'{key}, {value}\n') #сохранить в файл

#Отсортировать по значениям от меньшего к большему 

valuesort_a={value: a[value] for value in sorted(a)}

valuesort_a={value: key for key, value in valuesort_a.items()} 

#print('сортировка от меньшего к большему',valuesort_a)

with open('от меньшего к большему.txt', 'w') as file2:

  for key, value in valuesort_a.items():

    file2.write(f'{key}, {value}\n') #сохранить в файл

#Создать список из значений словаря и разделить его на два:

#один из значений меньше среднего по списку, второй - среднее и выше.

hige={} #для среднего и выше

low={} #для ниже среднего

sr_zn=sum(value for value in a.values())/8 #среднее знаение

for key,value in a.items():

    if value< sr_zn:

        low[key] = value

    else:

        hige[key]=value

print('больше среднего значения',hige)

print('меньше среднего значения',low)

    

#print(a)

