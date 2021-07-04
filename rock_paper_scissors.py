import random


def ask_option(options):
    print(f"Choose your weapon: {' | '.join(options)} | (q to quit)")
    return input(">> ").lower()


def handle_option(options, user_option):
    computer_option_idx = random.randrange(0, len(options))
    user_option_idx = options.index(user_option)

    if computer_option_idx == user_option_idx:
        print("It's a tie\n")
        return 0

    if (user_option_idx - 1) % len(options) == computer_option_idx:
        print(f"you win: {user_option} beats {options[computer_option_idx]}\n")
        return 1

    print(f"you lose: {options[computer_option_idx]} beats {user_option}\n")
    return -1


def play(options):
    score = [0, 0]
    while True:
        print(f"Current score: {' - '.join([str(p) for p in score])}")
        option = ask_option(options)
        if option == "q":
            break

        if option not in options:
            print("invalid option\n")
            continue

        outcome = handle_option(options, option)
        if outcome == 0:
            continue

        if outcome == 1:
            score[0] += 1
            continue

        score[1] += 1

    print("\n*** Thank you for playing ***")


def main():
    play([
        "rock", "paper", "scissors"
    ])


if __name__ == "__main__":
    main()
