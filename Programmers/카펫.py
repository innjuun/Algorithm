def solution(brown, yellow):
    for y in range(3, brown // 2):
        x = 3
        while x < brown // 2:
            if (x + y) * 2 - 4 == brown and y >= x and (x - 2) * (y - 2) == yellow:
                return [y, x]
            x += 1
