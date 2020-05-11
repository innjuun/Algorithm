"""
N = int(input())
count = [0 for i in range(10)]
cnt = 0
count[0] = 0
count[1] = 9
count[2] = count[1] + 2 * 90
count[3] = count[2] + 3 * 900
count[4] = count[3] + 4 * 9000
count[5] = count[4] + 5 * 90000
count[6] = count[5] + 6 * 900000
count[7] = count[6] + 7 * 9000000
count[8] = count[7] + 8 * 90000000
count[9] = count[8] + 9 * 900000000

if N < 10:
    cnt = count[0] + N
elif N >= 10 and N < 100:
    cnt = count[1] + 2 * (N - 9)
elif N >= 100 and N < 1000:
    cnt = count[2] + 3 * (N - 99)
elif N >= 1000 and N < 10000:
    cnt = count[3] + 4 * (N - 999)
elif N >= 10000 and N < 100000:
    cnt = count[4] + 5 * (N - 9999)
elif N >= 100000 and N < 1000000:
    cnt = count[5] + 6 * (N - 99999)
elif N >= 1000000 and N < 10000000:
    cnt = count[6] + 7 * (N - 999999)
elif N >= 10000000 and N < 100000000:
    cnt = count[7] + 8 * (N - 9999999)
elif N == 100000000:
    cnt += count[8] + 9

print(cnt)
"""

N = int(input())

start = 1
end = 0
length = 1
ans = 0
while start <= N:
    end = (start * 10) - 1
    if end > N:
        end = N

    ans = ans + (end - start + 1) * length
    start *= 10
    length += 1

print(ans)
