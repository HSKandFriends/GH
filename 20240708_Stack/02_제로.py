# https://www.acmicpc.net/problem/10773

import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]

answer = list()

for num in data:
    num = int(num)
    if num != 0:
        answer.append(num)
    else:
        answer.pop()

print(sum(answer))