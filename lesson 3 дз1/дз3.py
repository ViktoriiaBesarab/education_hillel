my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = [1, 2, 3, 4, 5]
my_list_3 = [1, ]
my_list_4 = []

if len(my_list_1) == 0:
    result =[[], []]
else:
    mid = (len(my_list_1) + 1) // 2
    result = [my_list_1[:mid], my_list_1[mid:]]

print(result)

if len(my_list_2) == 0:
    result =[[], []]
else:
    mid = (len(my_list_2) + 1) // 2
    result = [my_list_2[:mid], my_list_2[mid:]]

print(result)

if len(my_list_3) == 0:
    result =[[], []]
else:
    mid = (len(my_list_3) + 1) // 2
    result = [my_list_3[:mid], my_list_3[mid:]]

print(result)

if len(my_list_4) == 0:
    result =[[], []]
else:
    mid = (len(my_list_4) + 1) // 2
    result = [my_list_4[:mid], my_list_4[mid:]]

print(result)

