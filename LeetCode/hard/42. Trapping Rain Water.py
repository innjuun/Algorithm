class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_height = [0 for _ in range(len(height))]
        right_height = [0 for _ in range(len(height))]
        maximum = 0
        for i in range(len(height)):
            maximum = max(maximum, height[i])
            left_height[i] = max(maximum, height[i])
        maximum = 0
        for i in range(len(height)-1, -1, -1):
            maximum = max(maximum, height[i])
            right_height[i] = max(maximum, height[i])
        
        print(left_height, right_height)
        answer = 0
        for i in range(len(height)):
            answer += min(left_height[i], right_height[i]) - height[i]
        return answer
                