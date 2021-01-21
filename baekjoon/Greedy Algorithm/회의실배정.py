N = int(input())
case_list = []
for i in range(N):
    line = []
    for j in range(2):
        line.append(0)
    case_list.append(line)


for i in case_list:
    i[0], i[1] = map(int, input().split())
    i.reverse()

case_list.sort()

for i in case_list:
    i.reverse()

count = 0
start_time = 0
end_time = 0
for i in case_list:
    if i[0] >= end_time:
        start_time = i[0]
        end_time = i[1]
        count += 1

print(count)
