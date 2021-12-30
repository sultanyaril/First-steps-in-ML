def is_palindrome(x):
    if x != 0 and x % 10 == 0:
        return "NO"
    reverse_number = 0
    copy = x
    while copy != 0:
        reverse_number = reverse_number*10 + copy % 10
        copy //= 10
    if reverse_number == x:
        return "YES"
    return "NO"

if __name__ == "__main__":
   print(is_palindrome(101))
