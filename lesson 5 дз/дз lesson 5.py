import string

def your_text(text):
    for my_task in string.punctuation:
        text = text.replace(my_task, "")
    text = text.title()
    text = "#" + text.replace(" ", "")
    if len(text) > 140:
        text = text[:140]

    return text


your_text1 = input("Enter your text: ")
result = your_text(your_text1)
print(result)