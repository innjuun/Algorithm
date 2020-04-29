num = input()

li = [i for i in num]

print(li)

li.reverse()

print(li)
sum = 0
mul = 0
for i in range(len(li)):
    if li[i] == "1":
        sum += mul
    print(mul, sum)
    mul = mul*2
print(sum)
