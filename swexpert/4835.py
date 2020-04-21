T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    numbers = list(map(int, input().split()))[:N]
    adding = []



    for i in range(len(numbers)-M+1):
        sum = 0
        for j in range(M):
            sum += numbers[i+j]
        adding.append(sum)

    maximum = max(adding)
    minimum = min(adding)
    sorted

    result = maximum-minimum

    print('#{} {}'.format(test_case, result))