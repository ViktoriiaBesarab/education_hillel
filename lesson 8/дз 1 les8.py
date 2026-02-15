def add_one(some_list):
    new_lis = "".join(map(str, some_list))
    res = int(new_lis)
    res = res + 1
    result = list(map(int, str(res)))
    return result

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))


