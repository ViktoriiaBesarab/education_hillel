def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

is_palindrome('A man, a plan, a canal: Panama')
is_palindrome('0P')
is_palindrome('a.')
is_palindrome('aurora')

print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a'))
print(is_palindrome('aurora'))


