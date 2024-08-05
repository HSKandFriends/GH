# https://www.acmicpc.net/status?user_id=kgh5788&problem_id=2164&from_mine=1

import sys
from collections import deque

def solution(num:int) -> int:
    queue = deque(range(1, num+1))
    
    while True:
        if len(queue) == 1:
            return queue[0]
        else:
            queue.popleft()
            tmp = queue.popleft()
            queue.append(tmp)
    
n = int(sys.stdin.readline())

answer = solution(n)
print(answer)
