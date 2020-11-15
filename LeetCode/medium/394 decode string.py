class Solution:
    def decodeString(self, s: str) -> str:
        count = 0

        stack = []
        current_string = ""
        for i in s:
            if i.isdigit():

                count = count * 10 + int(i)
                
            elif i == "[":
                stack.append((current_string, count))
                count = 0
                current_string = ""

            elif i == "]":
                print(stack)
                prev_string, prev_count = stack.pop()
                current_string = prev_string + prev_count * current_string
    
                
            else:
                current_string += i

            
        return current_string