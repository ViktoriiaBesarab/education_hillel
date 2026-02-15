import string
import keyword

name = input("Enter name: ")
can_use = True
punct = string.punctuation.replace("_", " ")
item = "_"
if name[0].isdigit():
    can_use = False
elif any(a.isupper() for a in name):
    can_use = False
elif " " in name:
    can_use = False
#elif (item * 2) in name:
    #print(f"Символ '{item}' идет подряд 3 раза")
    #can_use = False
elif name in keyword.kwlist:
    can_use = False
elif any(h in punct for h in name):
    can_use = False

has_doubles = False
for i in range(len(name) - 1):
    if name[i] == name[i+1]:
        print(f"Символы {name[i]} идут подряд")
        has_doubles = True
        break

print(can_use)