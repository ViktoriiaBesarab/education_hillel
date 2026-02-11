seconds = int(input("Enter seconds : "))

if 0 <= seconds < 8640000:
    days = seconds // (24 * 60 * 60)
    amount = seconds % (24 * 60 * 60)
    hours = amount // (60 * 60)
    amount = amount % (60 * 60)
    minutes = amount // 60
    seconds = amount % 60
    if 11 <= days % 100 <= 14:
        day_word = "днів"
    elif days % 10 == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    print(f"{days} {day_word}, "
          f"{str(hours).zfill(2)}:"
          f"{str(minutes).zfill(2)}:"
          f"{str(seconds).zfill(2)}")
else:
    print("Enter number from 0 to 864000: ")