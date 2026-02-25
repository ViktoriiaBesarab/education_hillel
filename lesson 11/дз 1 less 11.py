import math

def prime_generator(end):
    if end <= 1:
        return

    for num in range(2, end + 1):

        if num == 2:
            yield num
            continue

        if num % 2 == 0:
            continue

        is_prime = True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

from inspect import isgenerator
gen = prime_generator(1)
isgenerator(gen)
result = list(prime_generator(10))
result_2 = list(prime_generator(15))
result_3 = list(prime_generator(29))
print(result)
print(result_2)
print(result_3)
print('Ok')
