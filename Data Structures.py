my_list = [1, 2, "Three", 4, 5, 6]

my_list[1] = 9

print(my_list)

my_list.append(7)

my_list.remove(4)
del my_list[0]

if 7 in my_list:
    print('Item is in list')
else:
    print('Item is not in list')

my_tuple = (1, "Two", 3, 3, 5, 6, my_list)

if 7 in my_tuple:
    print('Item is in list')
else:
    print('Item is not in list')

print(my_tuple)

my_set = {1, 2, 3, "Four", 5, 6}

my_set.add(7)

if 2 in my_set:
    my_set.remove(2)

print(my_set)

my_dict = {1: "Hello", 2: 4, "Three": 1, 4: 8}

del my_dict[4]

my_dict[1] = "Hej"
my_dict[5] = "Hej"

print(my_dict)

my_dict[1] = 1

if 5 in my_dict:
    print(f'key is in dict with value {my_dict[5]}')
else:
    print('key is not in dict')

for x, y in my_dict.items():
    print(x, y)

d = {i * 2: i * i for i in range(10)}

print(d)


squares_set_comp = {x*x for x in range(10)}

squares_dict_comp = {x: x*x for x in range(10)}

print(squares_set_comp)
print(squares_dict_comp)
