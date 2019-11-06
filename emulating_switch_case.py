def dispatch_if(operator, x, y):
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == "mul":
        return x * y
    elif operator == "div":
        return x / y
    return None


def dispatch_dict(operator, x, y):
    # Cache this dict in a variable if it gets too big / we use it too much
    # now we recreate this dict every time we call this dispatch function
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mul": lambda: x * y,
        "div": lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_dict("add", 8, 3))
print(dispatch_if("div", 12, 4))
