def find_longest_sub_array(arr, s):
    return_list = []
    for i in range(len(arr)):
        temp_list = [arr[i]]
        for j in range(i+1, len(arr)):
            temp_list.append(arr[j])

            if sum(temp_list) == s:
                # Only update if the new subarray is longer than the previous one
                if len(temp_list) > len(return_list):
                    return_list = temp_list
                    break

            elif sum(temp_list) > s:
                break

    return return_list


def find_longest_sub_array2(arr, s):
    start_index = 0
    end_index = 0

    for i in range(len(arr)):
        current_sum = arr[i]
        for j in range(i+1, len(arr)):
            current_sum += arr[j]

            if current_sum == s:
                # Only update if the new subarray is longer than the previous one
                if (end_index - start_index) < (j - i):
                    start_index = i
                    end_index = j
                    break

            elif current_sum > s:
                break

    # include the end index in the subarray
    return arr[start_index:end_index+1]


test_arr = [1, 2, 10, 2, 3, 7, 5, 1, 1, 1, 1, 3, 9]
test_s = 15

# method 1, creating with lists
result = find_longest_sub_array(test_arr, test_s)
print(result, sum(result))

# method 2, calculating with values
result2 = find_longest_sub_array2(test_arr, test_s)
print(result2, sum(result2))
