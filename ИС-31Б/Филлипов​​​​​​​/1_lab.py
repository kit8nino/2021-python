# 1
dict = {'ф': 22,'ф': 10,'л': 13,'и': 10,'п':17,'п':17,'о': 16,'в': 3}
def fact(a):
    if a == 0:
        return 1
    return fact(a-1) * a
for i in dict:
    dict[i] = fact(dict[i])
print(dict)

#2.
sorteddict =  sorted(dict.values())
sorted_dict = {}
for i in sorteddict:
  for j in dict.keys():
    if dict[j]==i:
      sorted_dict[j]= dict[j]
      break
print(sorteddict)
file_to_save = open('file1.txt', 'w+')
file_to_save.write(str(sorted_dict[j]))
file_to_save.close()

#3.
dict1 = {}
sorteddict1 = sorted(dict, key=dict.get)
for i in sorteddict1:
  dict1[i]= dict[i]
print(dict1)
file_to_save = open('file2.txt', 'w+')
file_to_save.write(str(sorteddict1))
file_to_save.close()

#4
dict2 = {'ф': 22,'ф': 10,'л': 13,'и': 10,'п':17,'п':17,'о': 16,'в': 3}
a = dict2.values()
mean = (sum(a) / len(a))
dict_small = [i for i in a if i < mean]
dict_big = [i for i in a if i > mean]
print('меньше среднего:', dict_small)
print('больше среднего:', dict_big)