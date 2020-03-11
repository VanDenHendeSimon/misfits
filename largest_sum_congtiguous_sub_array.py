def largest_sum_congtiguous_sub_array(arr):
    sub_array = []
    for i in range(len(arr)):
        temp_array = [arr[i]]

        for j in range(i+1, len(arr)):
            if (sum(temp_array) < sum(temp_array) + arr[j]) and sum(temp_array) + arr[j] > sum(sub_array):
                temp_array.append(arr[j])

            if sum(temp_array) > sum(sub_array):
                sub_array = temp_array

            else:
                break

    return sub_array


print(largest_sum_congtiguous_sub_array([-2, 2, 5, 10, -11, 6]))
print(largest_sum_congtiguous_sub_array([-2, -3, 4, -1, -2, 1, 5, -3]))
print(largest_sum_congtiguous_sub_array([-2, -3, 4, 8, 12, -8, 45, -1, -2, 1, 5, -3]))
