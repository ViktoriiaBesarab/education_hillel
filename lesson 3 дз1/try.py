price = int(input("enter price: "))
sale = int(input("enter sale: "))

size_sale = price * sale // 100
result = price - size_sale

print(result)