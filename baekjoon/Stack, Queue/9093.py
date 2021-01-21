T = int(input())
cases = []
for i in range(T):
    cases.append(input())

for case in cases:
    words = case.split(" ")
    for word in words:
        print(word[::-1], end="")
        print(end=" ")
    print()
