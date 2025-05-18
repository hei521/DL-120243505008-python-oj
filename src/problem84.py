def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

def is_palindrome_with_pointer(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

n = int(input())
strings = [input().strip() for _ in range(n)]

for s in strings:
    if is_palindrome(s) and is_palindrome_with_pointer(s):
        print(s)