def get_first_non_repeating_char(string, method):
    if method == "next":
        try:
            result = next(
                char for char in string
                if string.count(char) == 1
            )
        except Exception:
            result = "_"

        return result

    elif method == "loop":
        for char in string:
            if string.count(char) == 1:
                return char
        return "_"

    elif method == "dict":
        letters = dict()
        for char in string:
            if char in letters.keys():
                letters[char] += 1
            else:
                letters[char] = 1

        for char in string:
            if letters[char] == 1:
                return char

        return "_"


first_non_repeating_char = get_first_non_repeating_char("deeffdsqqafgdsg", "dict")
print("First non repeating char is '%s'" % first_non_repeating_char)
