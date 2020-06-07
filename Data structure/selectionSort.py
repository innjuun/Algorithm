"""
def selectionSort(list):
    for size in reversed(range(len(list))):
        max_i = 0

        for i in range(1, size+1):
            if list[i] > list[max_i]:
                max_i = i
        list[size], list[max_i] = list[max_i], list[size]
"""


def selectionSort(list):
    for size in range(len(list) - 1, -1, -1):
        max_i = 0
        for i in range(1, size + 1):
            if list[i] > list[max_i]:
                max_i = i
        list[size], list[max_i] = list[max_i], list[size]


"""

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1 + size):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)
"""

li = [1, 3, 4, 1, 5, 3, 6, 5]
selectionSort(li)
print(li)
