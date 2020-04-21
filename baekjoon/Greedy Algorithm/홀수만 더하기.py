T = int(input())
answer = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for i in range(T):
    result = set()
    N = str(input())
    K = N
    while result != answer:
        count = 1

        for i in N:
            if i not in result:
                result.add(i)
        count +=1
        N = K * count




        print(N)


