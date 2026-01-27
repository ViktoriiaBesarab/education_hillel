my_list_1 = [1, 15, 46, False, 25.5]
my_list_2 = []
my_list_3 = [0,]

my_list_1[4], my_list_1[0] = my_list_1[0], my_list_1[4]
my_list_1.pop(-1)
my_list_1.insert(1, 1)
print(my_list_1)

print(my_list_2)

my_list_3[-1], my_list_3[0] = my_list_3[-1], my_list_3[0]
my_list_3.pop(-1)
my_list_3.insert(1, 0)
print(my_list_3)

