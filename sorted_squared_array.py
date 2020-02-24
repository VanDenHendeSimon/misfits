def square_and_sort(_list):
    return sorted([
        n**2 for n in _list
    ])


the_list = [-6, -4, 1, 2, 3, 5]
print(type(square_and_sort(the_list)))
print(square_and_sort(the_list))
