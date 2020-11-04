# brute force, exceeded time limit
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T) 
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                if T[j] > T[i]:
                    answer[i] = j-i
                    break
        return answer
    
# stack

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(T)
        stack.append((T[0], 0))
        for i in range(1, len(T)):
            while stack and T[i] > stack[-1][0]:
                num, index = stack.pop()
                answer[index] = i - index
            stack.append((T[i], i))
            
        return answer