import string
import keyword

name = input("Enter name: ")
can_use = True

if name[0].isdigit():
    can_use = False
elif name.islower():
    can_use = False
elif " " in name:
    can_use = False
elif name in keyword.kwlist:
    can_use = False
elif any(h in string.punctuation for h in name):
    can_use = False

print(can_use)