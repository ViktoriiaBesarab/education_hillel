number_1 = int(input("enter a number: "))
number_2 = int(input("enter another number: "))
action = input("enter action: ")

if action == "+":
    print(number_1 + number_2)
elif action == "-":
    print(number_1 - number_2)
elif action == "*":
    print(number_1 * number_2)
elif action == "/":
    if number_2 != 0:
     print(number_1 / number_2)
    else:
     print("Error")

