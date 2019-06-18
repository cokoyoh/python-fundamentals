def is_palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True

    return False


print(is_palindrome('dade'))
print(is_palindrome('dad'))
print(is_palindrome('mom'))
print(is_palindrome('mirror'))
