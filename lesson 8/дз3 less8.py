def find_unique_value(some_list):
    for x in some_list:
       if some_list.count(x) == 1:
         return x



find_unique_value([1, 2, 1, 1])
find_unique_value([2, 3, 3, 3, 5, 5])
find_unique_value([5, 5, 5, 2, 2, 0.5])

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))