n, m = map(int, input().split())

array = [["" for _ in range(m)] for _ in range(n)]
nx, ny = [0, 1, 0, -1], [1, 0, -1, 0]

alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def is_can_go(x, y):
    if x >= 0 and y >= 0 and x < n and y < m and array[x][y] == "":
        return True
        


i, j, cnt, direction = 0, 0, 0, 0
while True:
    array[i][j] = alphabets[cnt % 26]
    if is_can_go(i + nx[direction % 4], j + ny[direction % 4]):
        pass
    else:
        direction += 1

    if all([all(line) for line in array]):
        break

print('\n'.join([' '.join(line) for line in array]))
