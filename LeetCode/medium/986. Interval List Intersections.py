# time, memory exceeded
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # first = [0 for _ in range(10000001)]
        # second = [0 for _ in range(10000001)]
        first = [(False, 0) for _ in range(10000000)]
        second = [(False, 0) for _ in range(10000000)]
        for note in firstList:
            for i, n in enumerate(range(note[0], note[1] + 1)):
                if i != 0:
                    first[n] = True, 1
                else:
                    first[n] = False, 1
        
        for note in secondList:
            for i, n in enumerate(range(note[0], note[1] + 1)):
                if i != 0:
                    second[n] = True, 1
                else:
                    second[n] = False, 1
        ret = []
        stack = []
        for i, (a, b) in enumerate(zip(first, second)):
            if stack and (a[0] is False or b[0] is False):
                ret.append([stack[0], stack[0] + len(stack) - 1])
                stack = []
    
            if a[1] == 1 and b[1] == 1 and (a[0] is True and b[0] is True):
                stack.append(i)
                
            elif not stack and a[1] == 1 and b[1] == 1 and (a[0] is False or b[0] is False):
                stack.append(i)
    
        return ret