"""
N = int(input())
M = int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
broken_buttons = list(map(int, input().split()))
for i in broken_buttons:
    buttons.remove(i)
current_channel = 100

print(buttons)

count = 0

for i in range(len(buttons)):
    for j in range(len(N)):
        number = 
"""

N = int(input())
M = int(input())
if M != 0:
    broken_buttons = list(input().split())
else:
    broken_buttons = []
minimum = abs(N - 100)
for i in range(1000000):

    flag = True
    c = str(i)

    for char in c:
        if char in broken_buttons:
            flag = False
            break

    if flag is True:
        diff = N - i
        if N - i < 0:
            diff = -diff
        if diff + len(str(i)) < minimum:
            minimum = diff + len(str(i))

print(minimum)
