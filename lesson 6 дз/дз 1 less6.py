import string

def all_letters(a):
    letters = input("enter your let: ")
    start, end = letters.split("-")
    index_1 = a.index(start)
    index_2 = a.index(end)

    return a[index_1:index_2 + 1]


print(all_letters(string.ascii_letters))