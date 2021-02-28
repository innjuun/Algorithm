# from collections import deque

# n, m, c = map(int, input().split())

# grid = [list(map(int, input().split())) for _ in range(n)]
# directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

# x, y = map(int, input().split())
# x, y = x-1, y-1

# customer = 2

# for _ in range(m):
#     x_s, y_s, x_e, y_e = map(int, input().split())
#     grid[x_s-1][y_s-1] = (customer, x_e-1, y_e-1)
    

# def is_customer(i, j):
#     try:
#         return grid[i][j][0] == 2
#     except:
#         return False


# def get_destination(i, j):
#     try:
#         return grid[i][j][1], grid[i][j][2]
#     except:
#         return False       

    
# def is_in_grid(i, j):
#     return i >= 0 and j >= 0 and i < n and j < n


# def is_wall(i, j):
#     return grid[i][j] == 1


# def is_valid_road(i, j, visited):
#     return is_in_grid(i, j) and not is_wall(i, j) and visited[i][j] is False


# def find_customer(i, j):
#     visited = [[False for _ in range(n)] for _ in range(n)]

#     queue = deque()
#     queue.append((i, j, 0))
#     memo = 0
#     customer_list = []
#     while queue:
#         pos = queue.popleft()
#         if memo != pos[2] and customer_list:
#             return sorted(customer_list, key=lambda x: x[0])[0]
#         memo = pos[2]
#         if is_customer(pos[0], pos[1]):
#             customer_list.append(pos)
#         visited[pos[0]][pos[1]] = True
#         for ni, nj in directions:
#             next_i, next_j, next_count = pos[0] + ni, pos[1] + nj, pos[2] + 1
#             if is_valid_road(next_i, next_j, visited):
#                 queue.append((next_i, next_j, next_count))
#     if customer_list:
#         return sorted(customer_list, key=lambda x: x[0])[0]
#     return -1, -1, -1

# def find_destination(i, j, destine_i, destine_j):
#     visited = [[False for _ in range(n)] for _ in range(n)]

#     queue = deque()
#     queue.append((i, j, 0))
#     while queue:
#         pos = queue.popleft()
#         if pos[0] == destine_i and pos[1] == destine_j:
#             return pos[0], pos[1], pos[2]
#         visited[pos[0]][pos[1]] = True
#         for ni, nj in directions:
#             next_i, next_j, next_count = pos[0] + ni, pos[1] + nj, pos[2] + 1
#             if is_valid_road(next_i, next_j, visited):
#                 queue.append((next_i, next_j, next_count))

#     return -1, -1, -1
# def simulate(x, y, c):
#     for _ in range(m):
#         x, y, count = find_customer(x, y)
#         # print(x, y)
#         if x == -1 and y == -1:
#             return -1
#         c -= count
#         if c < 0:
#             return -1

#         destine_i, destine_j = get_destination(x, y)
#         grid[x][y] = 0

#         x, y, count = find_destination(x, y, destine_i, destine_j)
#         # print(x, y)
        
#         if x == -1 and y == -1:
#             return -1
#         if c - count < 0:
#             return -1
#         c += count
#     return c


# print(simulate(x, y, c))


from collections import deque
from copy import deepcopy
n, m, c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

x, y = map(int, input().split())
x, y = x-1, y-1


customer_list = []
for _ in range(m):
    x_s, y_s, x_e, y_e = map(int, input().split())
    customer_list.append([(x_s-1, y_s-1), (x_e-1, y_e-1)])
    

def is_in_grid(i, j):
    return i >= 0 and j >= 0 and i < n and j < n


def is_wall(i, j):
    return grid[i][j] == 1


def is_valid_road(i, j, visited):
    return is_in_grid(i, j) and not is_wall(i, j) and visited[i][j] is False


def bfs(i, j):
    visited = [[False for _ in range(n)] for _ in range(n)]
    distances = deepcopy(grid)
    queue = deque()
    queue.append([i, j, 0])
    while queue:
        i, j, count = queue.popleft()
        visited[i][j] = True
        distances[i][j] = count
        for d in directions:
            next_i, next_j = i + d[0], j + d[1]
            if is_valid_road(next_i, next_j, visited):
                queue.append([next_i, next_j, count + 1])
    return visited, distances


def pop_shortest_customer(distances):
    li = []
    for i, customer in enumerate(customer_list):
        li.append([distances[customer[0][0]][customer[0][1]], customer[0][0], i])

    return customer_list.pop(sorted(li)[0][-1])


def simulate(x, y, c):
    for _ in range(m):
        
        visited, distances = bfs(x, y)
        customer, destination = pop_shortest_customer(distances)

        distance = distances[customer[0]][customer[1]]
        is_visited = visited[customer[0]][customer[1]]
        if distance == 0 and not is_visited:
            return -1
        if c - distance < 0:
            return -1
        c -= distance
        # print(c)
        visited, distances = bfs(customer[0], customer[1])
        distance = distances[destination[0]][destination[1]]
        is_visited = visited[destination[0]][destination[1]]

        if distance == 0 and not is_visited:
            return -1
        if c - distance < 0:
            return -1
        c += distance
        # print(c)
        x, y = destination[0], destination[1]
    return c



print(simulate(x, y, c))