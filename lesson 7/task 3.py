def second_index(text, some_str):
    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + len(some_str))
    if second == -1:
        return None
    return second

test_1 = second_index("sims", "s")
test_2 = second_index("find the river", "e")
test_3 = second_index("hi", "h")
test_4 = second_index("Hello, hello", "lo")

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print("OK")