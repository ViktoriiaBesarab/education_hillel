def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    cont = begin
    for _ in range(end):
        yield cont
        cont = func(cont)
    yield begin

from inspect import isgenerator

gen = some_gen(2, 4, pow)
isgenerator(gen)
list(gen)
print(isgenerator(gen))
print(list(gen))
