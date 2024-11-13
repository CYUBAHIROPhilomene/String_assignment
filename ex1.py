def is_it_palindrome(strings):
    result = []
    for x in strings:
        palindrome_status = x.lower() == x[::-1].lower() 
        result.append((x, palindrome_status))  
    return result

strings = ["madam", "hello", "racecar", "world"]
print(is_it_palindrome(strings))