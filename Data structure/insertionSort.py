def insertionSort(list):
    for size in range(1, len(list)):
        val = list[size]
        i = size
        while i > 0 and list[i - 1] > val:
            list[i], list[i - 1] = list[i - 1], list[i]
            i -= 1


li = [10, 9, 8, 5, 4, 3, 2, 1]

insertionSort(li)
print(li)
