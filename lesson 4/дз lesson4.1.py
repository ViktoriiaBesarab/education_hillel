my_list = [0, 1, 0, 12, 3]
#my_list =[0]
#my_list =[1, 0, 13, 0, 0, 0, 5]
#my_list =[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

i = 0
long = len(my_list)
while i < long:
    if my_list[i] == 0:
        my_list.pop(i)
        my_list.append(0)
        long -= 1
    else:
        i += 1

print(my_list)
