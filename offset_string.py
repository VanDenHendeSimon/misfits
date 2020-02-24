import math


def fit(value, in_min, in_max, out_min, out_max, rounding):
    input_range = in_max - in_min
    output_range = out_max - out_min

    relative_input = (value - in_min) / input_range
    relative_output = relative_input * output_range

    if rounding == "floor":
        return math.floor(relative_output + out_min)
    else:
        return math.ceil(relative_output + out_min)


def offset_string(string, offset):
    new_string = list(string)

    for index, char in enumerate(string):
        offset_char_ascii = ord(new_string[index]) + offset
        fitted_char_ascii = int(fit(offset_char_ascii, offset, 127 + offset, 32, 126, "ceil"))
        new_string[index] = chr(fitted_char_ascii)

    return "".join(new_string)


def reverse_offset_string(string, offset, result):
    new_string = list(string)

    for index, char in enumerate(string):
        print(new_string[index], ord(new_string[index]), result[index], ord(result[index]))
        fitted_char_ascii = int(fit(ord(new_string[index]), 32, 126, offset, 127 + offset, "floor")) - offset
        print(fitted_char_ascii, chr(fitted_char_ascii))
        new_string[index] = chr(fitted_char_ascii)

    return "".join(new_string)


original_string = "Mijn naam is Simon en mijn liefje is Lunie"
# encrypred_string = offset_string(original_string, 12)
reversed_string = reverse_offset_string("Xmnq7qggp7mu7]mprq7jq7pmnq7omjknj7mu7Xvqmj", 12, original_string)
print(original_string)
print(reversed_string)
