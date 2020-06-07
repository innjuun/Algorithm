"""
def mergeSort(x):
    print("splitting", x)
    if len(x) > 1:
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        print(x, "and", li, ri, i)

        while li < len(lx):
            x[i] = lx[li]
            li += 1
            i += 1
        while ri < len(rx):
            x[i] = rx[ri]
            ri += 1
            i += 1
        print("merging", x)
"""


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        rx = alist[:mid]
        lx = alist[mid:]
        mergeSort(lx)
        mergeSort(rx)

        # devide
        li = 0
        ri = 0
        i = 0
        while li < len(lx) and ri < len(rx):
            print(alist)
            if lx[li] < rx[ri]:
                alist[i] = lx[li]
                i += 1
                li += 1
            else:
                alist[i] = rx[ri]
                i += 1
                ri += 1

        while li < len(lx):

            alist[i] = lx[li]
            i += 1
            li += 1

        while ri < len(rx):
            print(alist)
            alist[i] = rx[ri]
            i += 1
            ri += 1


li = [2, 7, 5, 6, 1, 2, 4, 3]
mergeSort(li)
print(li)
