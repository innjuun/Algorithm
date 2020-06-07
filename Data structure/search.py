def linearSearch(li, x):
    for i in range(len(li)):
        if x == li[i]:
            return i
    return None


def binarySearch(li, first, last, x):
    if first > last:
        print(first, last, x)
        return
    mid = (first + last) // 2

    if li[mid] == x:
        return mid

    elif li[mid] > x:
        binarySearch(li, first, mid - 1, x)
    elif li[mid] < x:
        binarySearch(li, mid + 1, last, x)
    else:
        return


"""
def binarySearch(li, x):
    start = 0
    last = len(li)
    while start <= last:

        mid = (start + last) // 2

        if li[mid] == x:
            return mid
        elif li[mid] > x:
            last = mid - 1
        elif li[mid] < x:
            start = mid + 1
    return None

"""
li = [1, 6, 3, 7, 5, 3, 2]
li1 = [1, 2, 3, 4, 7, 9, 10, 13, 100]
print(binarySearch(li1, 0, len(li1), 8))
