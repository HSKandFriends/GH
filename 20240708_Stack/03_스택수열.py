# https://www.acmicpc.net/problem/1874

import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]

answer = list()
ls = list()
cnt = 0

for i in range(1, n+1):
    ls.append(i)
    answer.append('+')
    while True:
        if ls:
            if ls[-1] == int(data[cnt]):
                ls.pop()
                answer.append('-')
                cnt += 1
            else:
                break
        else:
            break

if ls:
    print('NO')
else:
    for a in answer:
        print(a)