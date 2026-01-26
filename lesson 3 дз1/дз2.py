my_list_1 = [1, 15, 46, False, 25.5]
my_list_2 = []
my_list_3 = [0,]

def mov_last_to_first(my_list) :
    if len(my_list):
        my_list.insert(0, my_list.pop())
    return my_list

print(mov_last_to_first(my_list_1))
print(mov_last_to_first(my_list_2))
print(mov_last_to_first(my_list_3))