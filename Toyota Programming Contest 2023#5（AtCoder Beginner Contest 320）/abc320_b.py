def center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest(s):
    if len(s) < 2:
        return s

    max_palindrome = ""
    
    for i in range(len(s)):
        palindrome1 = center(s, i, i)
        if len(palindrome1) > len(max_palindrome):
            max_palindrome = palindrome1

        palindrome2 = center(s, i, i + 1)
        if len(palindrome2) > len(max_palindrome):
            max_palindrome = palindrome2

    return len(max_palindrome)

a = input()
print(longest(a))

