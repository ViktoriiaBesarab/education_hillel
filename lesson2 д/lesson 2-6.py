a = 10
b = ("Bob")
c = "wite"
print(a, b, c, "Hello")
print()
print("End")

print(a, b, c, "Hello", sep="---")
print(a, b, c, "Hello", end="")
print("Next Line")
print("After Next Line")

with open("../output.txt", "w") as f:
    print(a, b, c, "Hello", file=f, sep= ("---"))