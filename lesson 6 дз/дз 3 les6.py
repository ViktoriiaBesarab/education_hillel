number = int(input("enter number: "))

while number > 9:
   num = 1
   while number > 0:
      num *= number % 10
      number //= 10
   number = num
   print(number)
print(number)