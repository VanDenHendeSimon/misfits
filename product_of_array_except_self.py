def do_the_thing(arr):
    result = []
    for i in range(len(arr)):
        product = 1

        for j in range(len(arr)):
            if i != j:
                product *= arr[j]

        result.append(product)
    return result


print(do_the_thing([1, 2, 3, 4]))
