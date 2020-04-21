T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    case_list = [0] * 30
    template = []
    for i in range(10):
        line = []
        for j in range(10):
            line.append(0)
        template.append(line)

    for i in range(N):
        case_list[i] = list(map(int, input().split()))
        if case_list[i][4] == 1:
            for j in range(case_list[i][0], case_list[i][2]+1):
                for k in range(case_list[i][1], case_list[i][3]+1):
                    template[j][k] +=1

        if case_list[i][4] == 2:
            for j in range(case_list[i][0], case_list[i][2]+1):
                for k in range(case_list[i][1], case_list[i][3]+1):
                    template[j][k] +=1
        

    sum = 0
    for i in template:
        sum += i.count(2)

    print('#{} {}'.format(test_case, sum))




