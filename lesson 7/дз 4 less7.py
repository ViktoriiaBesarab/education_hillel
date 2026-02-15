def common_elements():
    my_list_1 = []
    my_list_2 = []
    for i in range(0, 99):
        if ((i % 3) == 0):
            my_list_1.append(i)
        if ((i % 5) == 0):
            my_list_2.append(i)
    return my_list_1, my_list_2

list1, list2 = common_elements()
print(list1)
print(list2)

intersection = set(list1) & set(list2)
print(intersection)

