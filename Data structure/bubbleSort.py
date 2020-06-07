def bubbleSort(list):
    for i in range(len(list) - 1, -1, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


li = [1, 3, 4, 5, 6, 3, 7, 2]
bubbleSort(li)
print(li)
