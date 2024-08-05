# https://www.acmicpc.net/status?user_id=kgh5788&problem_id=2164&from_mine=1

import sys
from collections import deque

def solution(data:list) -> str:
    wait = deque()
    last_wait = 0
    max_wait = 0
    len_wait = 0
    
    for tmp in data:
        tmp = list(map(int, tmp.split()))
        if tmp[0] == 1:
            wait.append(tmp[1])
            len_wait += 1
        elif tmp[0] == 2:
            wait.popleft()
            len_wait -= 1
            
        if max_wait < len_wait:
            max_wait = len_wait
            last_wait = wait[-1]
        elif max_wait == len_wait:
            if wait[-1] < last_wait:
                last_wait = wait[-1]

    return f'{max_wait} {last_wait}'
    
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]

answer = solution(data)
print(answer)
