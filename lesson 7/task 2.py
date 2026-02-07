def correct_sentence(text):
    text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text


test_1 = correct_sentence("greetings, friends")
test_2 = correct_sentence("hello")
test_3 = correct_sentence("Greetings. Friends")
test_4 = correct_sentence("Greetings, friends.")
test_5 = correct_sentence("greetings, friends.")

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)
