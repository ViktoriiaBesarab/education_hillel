my_list = [0, 1, 7, 2, 4, 8]
#my_list = [6]
#my_list = []

if my_list:
    sum = 0
    for index, number in enumerate(my_list):
        if index % 2 == 0:
         sum += number
    last = my_list[-1]
    result = sum * last
    print(result)
else:
    print("Empty list")