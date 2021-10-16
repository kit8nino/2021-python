mixed_list = [3, -42345, 'eras', (3+5j), '173', 65535, -391.327, None]
filtered_list = [x for x in mixed_list if x != None]
dict_list = {'int': 16768, 'float': -1.3273, 'str': 'foo_cad', 'complex':(5 + 1.3j), 'ept':None}
tuple_list = (3, 1, .32, 'ryry', -3221.3221, None, None)
filt_dict = {key: value for key, value in dict_list.items() if len(key) > 3 or value != None}
print(filt_dict)
print(filtered_list)