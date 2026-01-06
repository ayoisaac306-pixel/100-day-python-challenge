def is_palindrome(text):
    # conver to lower and remove space
    text = text.lower().replace(" ", "")
    return text == text[: : -1]

word = input("Enter text")

if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")    
