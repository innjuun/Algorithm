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


# def quickSort(list, start, end):
#     if start < end:
#         pivot = partition(list, start, end)

#         quickSort(list, start, pivot - 1)
#         quickSort(list, pivot, end)
#     return list


# def partition(list, start, end):
#     wall = start
#     left = start
#     pivot = end

#     while left < pivot:

#         if list[left] < list[pivot]:
#             list[wall], list[left] = list[left], list[wall]
#             wall += 1
#         left += 1

#     list[wall], list[pivot] = list[pivot], list[wall]

#     pivot = wall
#     return pivot


def quicksort(nums, start, end):
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)
    return nums


def partition(nums, start, end):
    wall = start
    for left in range(start, end):
        if nums[left] < nums[end]:
            nums[left], nums[wall] = nums[wall], nums[left]
            wall += 1
    nums[wall], nums[end] = nums[end], nums[wall]

    return wall


li = [4, 3, 2, 1, 2, 3, 5, 2, 6, 4, 2, 53, 214, 2, 1, 4, 2, 8]
print(quicksort(li, 0, len(li) - 1))
