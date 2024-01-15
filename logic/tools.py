import re


def roman_to_arabic(s: str) -> str:
    equals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    parts = list(reversed([equals[char] for char in s]))

    current_num = parts.pop(0)
    result = current_num
    while len(parts) > 0:
        next_num = parts.pop(0)
        if next_num < current_num:
            result -= next_num
        else:
            result += next_num
            current_num = next_num

    return str(result)


def replace_all_romans(s: str) -> str:
    return re.sub('[XVI]{1,6}', lambda x: roman_to_arabic(x.group()), s)
