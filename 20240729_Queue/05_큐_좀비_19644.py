# https://www.acmicpc.net/problem/19644

import sys
from collections import deque

input = sys.stdin.readline

def solution(length:int, ran:int, att:int, cammo:int, zombie:deque) -> str:
    cnt = 0

    while zombie:
        cnt += 1
        if zombie[0]-cnt*att <= 0:
            zombie.popleft()
        else:
            if cammo:
                cnt -= 1
                cammo -= 1
                zombie.popleft()
            else:
                return 'NO'
    return 'YES'
     
length = int(input())
ran, att = map(int, input().strip().split())
cammo = int(input())

zombie = deque()
for i in range(length):
    tmp = int(input())
    if ran <= i:
        zombie.append(tmp + att*(i-ran+1))
    else:
        zombie.append(tmp)

answer = solution(length, ran, att, cammo, zombie)
print(answer)
