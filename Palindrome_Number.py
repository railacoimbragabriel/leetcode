
def isPalindrome(x: int) -> bool:
    x_str = str(x)
    if x_str == x_str[::-1]:
        return True
    else:
        return False


print(isPalindrome(10))
