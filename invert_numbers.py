def reverse_number(number):
    """
    1) Convert number to a string and trim away the zeros that are on the right
    2) Convert that string into a list, and reverse it ([::-1])
    3) In case the input number is negative, strip out the - sign
    4) Join that list back to a string with no seperation
    5) Convert back to integer
    :param number: any integer to reverse
    :return: the given number, reversed, without zero-padding
    """
    if number > 0:
        return int("".join(list(str(number).rstrip("0"))[::-1]))
    else:
        return -int("".join(list(str(number).rstrip("0"))[::-1][:-1]))


nr = -1203405430000
# zeros on the end should be trimmed
print(reverse_number(nr))
