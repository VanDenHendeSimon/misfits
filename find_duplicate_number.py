import random


def find_smallest_duplicate_number(numbers):
    # _numbers = []
    # for i in sorted(numbers):
    #     if i not in _numbers:
    #         _numbers.append(i)
    #     else:
    #         return i

    numbers = list(sorted(numbers))
    # for i in range(len(numbers)):
    #     if numbers[i] == numbers[i+1]:
    #         return numbers[i]

    for i, number in enumerate(numbers):
        if number == numbers[i+1]:
            return number


def find_all_duplicate_numbers(numbers):
    _numbers = []
    duplicates = []
    for i in sorted(numbers):
        if i not in _numbers:
            _numbers.append(i)
        else:
            if i not in duplicates:
                duplicates.append(i)

    return duplicates


def generate_numbers(amount):
    return [random.randint(1, amount) for _ in range(amount+1)]


def main():
    numbers = generate_numbers(6)
    smallest_duplicate_number = find_smallest_duplicate_number(numbers)
    duplicate_numbers = find_all_duplicate_numbers(numbers)
    print(smallest_duplicate_number, duplicate_numbers, numbers)


if __name__ == '__main__':
    main()
