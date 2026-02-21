def difference(*args):
    if not args:
        return 0

    result = max(args) - min(args)
    return round(result, 2)

print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())
print('OK')
