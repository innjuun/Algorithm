from collections import deque

N, K = input().split()
# people = [i+1 for i in range(int(N))]
queue_people = deque()
# print(people)
for i in range(int(N)):
    queue_people.append(i+1)
li = []
while queue_people:
    for i in range(int(K)-1):
        queue_people.append(queue_people.popleft())
    li.append(str(queue_people.popleft()))

print("<" + ", ".join(li) + ">")
