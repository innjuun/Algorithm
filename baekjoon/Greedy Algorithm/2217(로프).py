N = int(input())
case_list = [0]*N
for i in range(N):
    case_list[i] = int(input())

case_list.sort()
case_list.reverse()
maximum = 0
for i in range(N):
    if case_list[i] * (i+1) > maximum:
        maximum = case_list[i] * (i+1)

print(maximum)
# final_rope = 0
# for i in range(N):
#     if final_rope >= i*final_rope:
#         final_rope = case_list[i]
# print(final_rope)
# sum = 0
# rope_index = case_list.index(final_rope)
# for i in range(rope_index):
#     sum += i
# result = sum / rope_index
# print(rope_index)
# print(result)