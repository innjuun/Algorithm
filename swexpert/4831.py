T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = int(input())
    stations = []
    charger = list(map(int, input().strip().split()))[:M]
    count= 0
    for i in range(N):
        stations.append(0)
    for i in range(M):
        stations[charger[i]] += 1

    charger.
    charger.append(N)

    for i in range(M):
        if charger[i+1] - charger[i] >K:

            count+=1
        else
