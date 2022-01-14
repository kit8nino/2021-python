import math
letter=['П','Р','О','Х','О','Р','О','В']
number=[17,18,16,23,16,18,16,3]
value=[]
for z in number:
    value.append(math.factorial(z))
a={k:v for k, v in zip(letter,value)}


keysort_a={k: a[k] for k in sorted(a)}
with open('alphabetically.txt', 'w') as file1:
  for letter, value in keysort_a.items():
    file1.write(f'{letter}, {value}\n')


valuesort_a={value: a[value] for value in sorted(a)}
valuesort_a={value: letter for letter, value in valuesort_a.items()}
with open('from-small-to-big.txt', 'w') as file2:
  for letter, value in valuesort_a.items():
    file2.write(f'{letter}, {value}\n')

big={}
avg={}
middle=sum(value for value in a.values())/8
for letter,value in a.items():
    if value< middle:
        avg[letter] = value
    else:
        big[letter]=value
print('больше среднего значения',big)
print('меньше среднего значения',avg)