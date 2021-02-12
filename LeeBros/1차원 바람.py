n, m, q = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]
winds = [input().split() for _ in range(q)]

winds = [(int(r), d) for r, d in winds]


def is_right_line(line):
    return line >= 0 and line < n


def wind_from_left(li):
    li.insert(0, li.pop())


def wind_from_right(li):
    li.append(li.pop(0))


def is_spreadable(origin, comp):
    return any([a == b for a, b in zip(origin, comp)])


for line, direction in winds:
    line -= 1
    if direction == "L":
        wind_from_left(array[line])
        
    elif direction == "R":
        wind_from_right(array[line])
    
    up = (line, direction)
    down = (line, direction)

    while True:
        line, direction = up
        if is_right_line(line - 1) and is_spreadable(array[line - 1], array[line]):
            curr = 0
            if direction == "L":
                curr = "R"
                wind_from_right(array[line - 1])
            elif direction == "R":
                curr = "L"
                wind_from_left(array[line - 1])
        else:
            break
        up = (line - 1, curr)

    while True:
        line, direction = down
        if is_right_line(line + 1) and is_spreadable(array[line + 1], array[line]):
            curr = 0
            if direction == "L":
                curr = "R"
                wind_from_right(array[line + 1])
            elif direction == "R":
                curr = "L"
                wind_from_left(array[line + 1])
        else:
            break
        down = (line + 1, curr)

[print(' '.join(map(str, array[i]))) for i in range(n)]