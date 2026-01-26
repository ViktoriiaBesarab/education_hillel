my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = [1, 2, 3, 4, 5]
my_list_3 = [1, ]
my_list_4 = []

def my_list(my_list):
    mid = (len(my_list) + 1) //2
    return [my_list[:mid], my_list[mid:]]

print(my_list(my_list_1))
print(my_list(my_list_2))
print(my_list(my_list_3))
print(my_list(my_list_4))