def generate_cube_numbers(end):
    number = 2
    for number in range(2, end):
        cube = number ** 3
        if cube > end:
          return
        yield cube

from inspect import isgenerator

gen = generate_cube_numbers(1)
isgenerator(gen)
result_1 = list(generate_cube_numbers(10))
result_2 = list(generate_cube_numbers(100))
result_3 = list(generate_cube_numbers(1000))
print(result_1)
print(result_2)
print(result_3)