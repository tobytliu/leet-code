import re

def valid_palindrome(s):
    s = s.lower().replace(" ", "")
    s = re.sub(r'[^a-zA-Z0-9]+', '', s)
    print(s)
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))
