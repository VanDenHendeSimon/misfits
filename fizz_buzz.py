def fizz_buzz(n):
    for i in range(1, n+1):
        to_print = ''
        to_print += 'Fizz' if (i % 3 == 0) else ''
        to_print += 'Buzz' if (i % 5 == 0) else ''

        print(
            to_print if to_print != '' else i
        )


if __name__ == '__main__':
    fizz_buzz(15)
