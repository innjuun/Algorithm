from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    checked = [0] * len(words)
    first= True
    queue.append(begin)
    while queue:
        num =queue.popleft()
        
        for w in range(len(words)):
            cnt = 0
            if checked[w] == 0:
                for i in range(len(words[w])):
                    if words[w][i] != num[i]:
                        cnt += 1
                if cnt == 1:
                    if first == True:
                        checked[w] = 1
                    else:
                        checked[w] = checked[words.index(num)] + 1
                    queue.append(words[w])
        first = False
        print(queue)
        
    
    print(checked) 
    return checked[words.index(target)]