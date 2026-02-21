def is_even(number):
    my_list = [0, 2, 4, 6, 8]
    last_digit = str(number)[-1]
    return int(last_digit) in my_list

print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))
