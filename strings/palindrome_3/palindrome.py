import re


def clean_string(string: str) -> str:
    return re.sub("[^A-Za-z0-9]", "", string.lower())


def is_valid_palindrome(string: str) -> bool:
    string = clean_string(string)

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_sub_palindrome(string: str, start: int, end: int) -> bool:
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def almost_palindrome(string: str) -> bool:
    string = clean_string(string)
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return valid_sub_palindrome(string, start + 1, end) or valid_sub_palindrome(string, start, end - 1)
        start += 1
        end -= 1
    return True
