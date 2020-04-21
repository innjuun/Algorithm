T = int(input())

for test_case in range(T):
    case_list = []
    N = int(input())
    for t in range(N):
        list = []
        for k in range(2):
            list.append(0)
        case_list.append(list)

    for i in range(N):
        case_list[i][0], case_list[i][1] = map(int, input().split())

    case_list.sort()
    print(case_list)


    # count = 0
    # survive1 = [False] * N
    # for i in range(N):
    #
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         if case_list[i][0] < case_list[j][0] or case_list[i][1] < case_list[j][1]:
    #             survive1[i] = True
    #     print(survive1)
    #     if survive1[i] !=True:
    #         count += 1
    # result = N - count
    # print(count)
