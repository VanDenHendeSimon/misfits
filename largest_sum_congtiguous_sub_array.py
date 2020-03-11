def largest_sum_congtiguous_sub_array(arr):
    sub_array = []
    for i in range(len(arr)):
        temp_array = [arr[i]]
        negative_values = []

        for j in range(i+1, len(arr)):
            if sum(temp_array) > sum(temp_array) + arr[j]:
                negative_values.append(arr[j])

            else:
                if sum(negative_values) + sum(temp_array) + arr[j] > sum(temp_array):
                    # add all negative values first
                    [temp_array.append(negative_value) for negative_value in negative_values]
                    temp_array.append(arr[j])

                else:
                    negative_values.append(arr[j])

        if sum(temp_array) > sum(sub_array):
            sub_array = temp_array

    return sub_array


print(largest_sum_congtiguous_sub_array([-2, 2, 5, 10, -11, 6]))
print(largest_sum_congtiguous_sub_array([-2, -3, 4, -1, -2, 1, 5, -3]))
print(largest_sum_congtiguous_sub_array([-2, -3, 4, 8, 12, -8, 45, -1, -2, 1, 5, -3]))
