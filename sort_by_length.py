def sort_by_length(_list):
    return list(sorted(_list, key=len))


if __name__ == '__main__':
    list_to_sort = [
        'Telescopes', 'Glasses', 'Eyes', 'Monocles'
    ]
    sorted_list = sort_by_length(list_to_sort)
    print('Initial list:', list_to_sort)
    print('Sorted list:', sorted_list)
