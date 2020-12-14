# class Solution:
#     def trap(self, height: List[int]) -> int:
        
#         left_height = [0 for _ in range(len(height))]
#         right_height = [0 for _ in range(len(height))]
#         maximum = 0
#         for i in range(len(height)):
#             maximum = max(maximum, height[i])
#             left_height[i] = max(maximum, height[i])
#         maximum = 0
#         for i in range(len(height)-1, -1, -1):
#             maximum = max(maximum, height[i])
#             right_height[i] = max(maximum, height[i])
        
#         print(left_height, right_height)
#         answer = 0
#         for i in range(len(height)):
#             answer += min(left_height[i], right_height[i]) - height[i]
#         return answer
                
# using stack       
class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []
        
        for i in range(len(height)):
            # print(stack, volume)
            
            
            while stack and height[i] >= height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                water_depth = min(height[stack[-1]], height[i]) - height[top]
                volume += distance * (water_depth)
            
            stack.append(i)
        
        return volume
    
# two pointer

class Solution:
    def trap(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        left_max = 0
        right_max = 0
        answer = 0
        while start <= end:
            print(start, end, answer)
            if height[start] <= height[end]:
                left_max = max(left_max, height[start])
                answer += left_max - height[start]
                start += 1
            else:
                right_max = max(right_max, height[end])
                answer += right_max - height[end]
                end -= 1
                
        return answer