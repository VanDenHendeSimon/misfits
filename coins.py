def min_coins(cents):
    coins = [50, 20, 10, 5, 2, 1]
    n_coins = 0
    feedback = ''

    for coin in coins:
        div = int(cents / coin)

        n_coins += div
        cents -= div*coin

        if div > 0:
            feedback += '%d x %d, ' % (div, coin)
        if cents == 0:
            break

    return n_coins, feedback


num_coins, user_feedback = min_coins(31)

print(num_coins, 'coins')
print(user_feedback)
