import string
import keyword

name = input("Enter name: ")
can_use = True
punct = string.punctuation.replace("_", " ")

if name[0].isdigit():
    can_use = False
elif any(a.isupper() for a in name):
    can_use = False
elif " " in name:
    can_use = False
elif name.count("_") > 1:
    can_use = False
elif name in keyword.kwlist:
    can_use = False
elif any(h in punct for h in name):
    can_use = False

print(can_use)