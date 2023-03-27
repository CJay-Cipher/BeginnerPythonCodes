"""Middle letter

Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return None.

For example, mid("abc") should return "b" and mid("aaaa") should return ""."""

def mid(word):
    num = len(word)
    return word[num // 2] if num % 2 == 1 else None


print(mid("trust"))