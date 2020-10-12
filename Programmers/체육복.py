def solution(n, lost, reserve):
    students = [True for i in range(n)]
    for lo in lost:
        students[lo-1] = False
    reserve = sorted(reserve)
    
    students = []
    for re in reserve.copy():
        if students[re-1] is False:
            students[re-1] = True
            reserve.remove(re)
            continue
    for re in reserve:
        if students[re - 2] is False:
            students[re-2] = True
        elif re <= n -1 and students[re] is False:
            students[re] = True
            
    return students.count(True)

solution(5, [2,4], [1,3,5])