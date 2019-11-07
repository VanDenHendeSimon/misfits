import math

names = [
    "a", "b", "c", "d", "e", "f", "g",  "h", "i", "j", "k", "l", "m", "n"
]

group_size = 3
group_amount = math.ceil(len(names) / group_size)

# For loop
groups = []
for i in range(group_amount):
    this_group = []
    for idx, name in enumerate(names):
        if idx % group_amount == i:
            this_group.append(name)
    groups.append(this_group)
print(groups)

# List comprehension
groups = []
for i in range(group_amount):
    groups.append(
        [name for idx, name in enumerate(names) if idx % group_amount == i]
    )
print(groups)

# Double list comprehension
groups = [
    [name for idx, name in enumerate(names) if idx % group_amount == i]
    for i in range(group_amount)
]
print(groups)
