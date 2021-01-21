import random


def compute_patterns(inputs=None):
    if inputs is None:
        inputs = {}
    inputs[random.randint(0, 100)] = random.randint(0, 100)
    return inputs, id(inputs)


print(compute_patterns())

print(compute_patterns())
print(compute_patterns())
