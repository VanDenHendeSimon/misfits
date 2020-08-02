def insertion_sort(arr):
    sorted_arr = [arr[0]]
    arr = arr[1:]

    for idx, value in enumerate(arr):
        desired_idx = 0
        for sorted_idx, sorted_value in enumerate(sorted_arr[::-1]):
            print(sorted_arr)
            if value < sorted_value:
                print("%s is smaller than %s" % (value, sorted_value))
                desired_idx = len(sorted_arr) - sorted_idx - 1
            else:
                print("%s is bigger than %s" % (value, sorted_value))
                desired_idx = len(sorted_arr) - sorted_idx
                break

        sorted_arr.insert(desired_idx, value)

    return sorted_arr


if __name__ == '__main__':
    result = insertion_sort([
        4, 5, 8, 1, 15, 3, 6, 9, 7
    ])

    print(result)
