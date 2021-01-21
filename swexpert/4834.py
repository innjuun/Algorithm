T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = str(input())
    count = [0 for i in range(10)]
    for i in range(len(a)):
        count[int(a[i])] += 1
    maximum = max(count)
    maximum_index = 0

    for i in range(len(count)):
        if maximum == count[i]:
            maximum_index = i

    print("#{} {} {}".format(test_case, maximum_index, maximum))
