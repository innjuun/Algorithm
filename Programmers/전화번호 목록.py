# def solution(phone_book):
#     dic = {}
#     phone_book = list(map(str, phone_book))
#     for e, p in enumerate(phone_book):
#         dic[e] = p

#     for d in dic:
#         tmp = dic.pop(d)
#         for value in dic.values():
#             if value.startswith(tmp):
#                 return False
#         dic[d] = tmp

#     return True

# my solution
def solution(phone_book):
    phone_book = list(map(str, phone_book))

    for i in phone_book:
        for j in phone_book:
            if i == j:
                continue
            if i.startswith(j):
                return False

    return True


# hash
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


solution([119, 97674223, 1195524421])
