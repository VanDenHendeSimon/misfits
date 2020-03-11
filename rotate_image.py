def rotate_image(img):
    """
    Rotates an image clockwise
    :param img: array of rows and columns
    :return: the same list, rotated by 90 degrees clockwise
    """
    r_img = []
    amount_of_collumns = len(img[0])

    for col in range(amount_of_collumns):
        t = []
        for row in reversed(img):
            t.append(row[col])
        r_img.append(t)

    return r_img


_img = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

_img2 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
]

rotated_img = rotate_image(_img)

print("before")
print(_img)
print("after")
print(rotated_img)
