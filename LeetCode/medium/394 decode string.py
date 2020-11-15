class Solution:
    def decodeString(self, s: str) -> str:
        count = 0

        stack = []
        current_string = ""
        for i in s:
            if i.isdigit():

                count = count * 10 + int(i)
                
            elif i == "[":
                stack.append((current_string, count ))
                count = 0
                current_string = ""

            elif i == "]":
                print(stack)
                string, count = stack.pop()
                current_string = string + count * current_string
                
                
            else:
                current_string += i

            
        return current_string