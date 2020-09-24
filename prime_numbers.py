def is_prime(number):

    # Catch accidentally returning True on 4 since the loop is not triggered
    limit = number // 2 if number // 2 > 2 else number

    for j in range(2, limit):
        if number % j == 0:
            print("%d = %dx%d" % (
                number, j, (number / j)
            ))

            return False

    return True


def main(n):

    # A Prime number is a number that is divisible only by itself and 1
    # The prime numbers below 20 are: 2, 3, 5, 7, 11, 13, 17, 19

    prime_numbers = []
    for i in range(2, n+1):
        if i <= 3:
            # 2 and 3 are prime, no need to check
            prime_numbers.append(str(i))
        else:
            if is_prime(i):
                prime_numbers.append(str(i))

    print("\nThe following numbers are prime: \n%s" % ', '.join(prime_numbers))


if __name__ == '__main__':
    main(100)
