import string
def your_text():
    your_text = input("Enter your text: ")
    your_text = your_text.title()
    your_text = "#" + your_text.replace(" ", "")
    if len(your_text) > 140:
        your_text = your_text[:140]
    for task in string.punctuation:
        your_text = your_text.replace(task, "")

    return your_text

print(your_text())


#age = input("Enter your age:")

#print(age + 10)
