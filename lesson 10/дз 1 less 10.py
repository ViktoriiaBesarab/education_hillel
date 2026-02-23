def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    current = begin
    for _ in range(end):
        yield current
        current = func(current)
    yield begin

from inspect import isgenerator

gen = some_gen(2, 4, pow)
isgenerator(gen)
list(gen)
print(isgenerator(gen))
print(list(gen))
