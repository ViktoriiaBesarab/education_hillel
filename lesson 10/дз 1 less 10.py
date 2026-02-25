def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    cont = begin
    for _ in range(end):
        yield cont
        cont = func(cont)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
isgenerator(gen)
result = list(gen)
print(isgenerator(gen))
print(result)
