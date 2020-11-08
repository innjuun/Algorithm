class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for i in s:
            if i == '(' or i =='[' or i=='{':
                a.append(i)
            
            if not a:
                return False
            else:
                if i == ')':
                    if a[-1] == '(':
                        a.pop()
                    else:
                        return False
                if i == ']':
                    if a[-1] == '[':
                        a.pop()
                    else:
                        return False

                if i == '}':
                    if a[-1] == '{':
                        a.pop()
                    else:
                        return False

        
        if not a:
            return True