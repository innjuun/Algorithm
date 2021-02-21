# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(S):
#     # write your code in Python 3.6
#     stack = []
    
#     operations = S.split()
#     try:
#         for operation in operations:
#             if operation == "POP":
#                 stack.pop()
#             elif operation == "DUP":
#                 stack.append(stack[-1])
#             elif operation == "+":
#                 last = stack.pop()
#                 stack.append(last + stack.pop())
#             elif operation == "-":
#                 last = stack.pop()
#                 stack.append(last - stack.pop())
#             else:
#                 stack.append(int(operation))
#     except IndexError:
#         return -1

#     return stack[-1]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def NegativeValueError(Exception):
    pass

def IntegerOverFlowError(Exception):
    pass
def solution(S):
    # write your code in Python 3.6
    stack = []
    maximum = 2 ** 20

    operations = S.split()
    try:
        for operation in operations:
            if operation == "POP":
                stack.pop()

            elif operation == "DUP":
                stack.append(stack[-1])

            elif operation == "+":
                last = stack.pop()
                second_last = stack.pop()
                if last + second_last >= maximum:
                    raise IntegerOverFlowError()
                stack.append(last + second_last)

            elif operation == "-":
                last = stack.pop()
                second_last = stack.pop()
                if last - second_last < 0:
                    raise NegativeValueError()
                stack.append(last - second_last)

            else:
                stack.append(int(operation))

    except Exception:
        return -1

    return stack[-1] if stack else -1

solution('3 DUP 5 - -')