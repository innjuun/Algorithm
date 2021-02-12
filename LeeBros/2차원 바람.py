from copy import deepcopy

n, m, q = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
winds = [list(map(int, input().split())) for _ in range(q)]
winds = [(wind[0]-1, wind[1]-1, wind[2]-1, wind[3]-1) for wind in winds]

arounds = [[0, 0], [0, -1], [0, 1], [1, 0], [-1, 0]]


def is_valid(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def rotate(array, wind):
    r1, c1, r2, c2 = wind
    current = r1, c1
    before_value = array[r1][c1]

    while current[1] < c2:
        new_value = array[current[0]][current[1]]
        array[current[0]][current[1]] = before_value
        before_value = new_value
        current = current[0], current[1] + 1
        
    while current[0] < r2:
        new_value = array[current[0]][current[1]]
        array[current[0]][current[1]] = before_value
        before_value = new_value
        current = current[0] + 1, current[1]

    while current[1] > c1:
        new_value = array[current[0]][current[1]]
        array[current[0]][current[1]] = before_value
        before_value = new_value
        current = current[0], current[1] - 1

    while current[0] >= r1:
        new_value = array[current[0]][current[1]]
        array[current[0]][current[1]] = before_value
        before_value = new_value
        current = current[0] - 1, current[1]


def change(array, wind):
    before_array = deepcopy(array)
    r1, c1, r2, c2 = wind

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            total = count = 0
            for around in arounds:
                if is_valid(i + around[0], j + around[1]):
                    count += 1
                    total += before_array[i + around[0]][j + around[1]]
            array[i][j] = total // count


for wind in winds:
    rotate(array, wind)
    change(array, wind)

for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print()