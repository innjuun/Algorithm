"""
def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quickSort(list, start, pivot - 1)
        quickSort(list, pivot + 1, end)
    return list


def partition(list, start, end):
    pivot = end
    wall = start
    left = start

    while left < pivot:

        if list[left] < list[pivot]:
            list[wall], list[left] = list[left], list[wall]
            wall += 1
        left += 1

    list[wall], list[pivot] = list[pivot], list[wall]
    pivot = wall
    return pivot
"""


def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)

        quickSort(list, start, pivot - 1)
        quickSort(list, pivot, end)
    return list


def partition(list, start, end):
    wall = start
    left = start
    pivot = end

    while left < pivot:

        if list[left] < list[pivot]:
            list[wall], list[left] = list[left], list[wall]
            wall += 1
        left += 1

    list[wall], list[pivot] = list[pivot], list[wall]

    pivot = wall
    return pivot


li = [0,7,2,5,3]
print(quickSort(li, 0, len(li) - 1))
