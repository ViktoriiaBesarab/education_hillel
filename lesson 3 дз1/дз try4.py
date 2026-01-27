my_list = [1, 15, 46, False, 25.5]
my_list2 = []
my_list3 = [0,]


if len(my_list) > 1 :
    new_list = my_list.pop(-1)
    my_list.insert(0, new_list)
    print(my_list)

if len(my_list2) > 1 :
    new_list = my_list2.pop(-1)
    my_list2.insert(0, new_list)
    print(my_list2)
else:
    print(my_list2)

if len(my_list3) > 1 :
    new_list = my_list3.pop(-1)
    my_list3.insert(0, new_list)
    print(my_list3)
else:
    print(my_list3)
