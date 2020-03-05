def factorial(factor):
    result = 1
    while factor > 0:
        result *= factor
        factor -= 1

    return result


def factorial_recursion(n):
    # 5! = 5 x 4!
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n - 1)


# print(factorial(5))
print(factorial_recursion(5))
