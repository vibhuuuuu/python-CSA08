def is_palindrome(s):
    
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
result = is_palindrome(s)
print(result)
