# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities:list, location:str):
    queue = deque()
    for idx, q in enumerate(priorities):
        flag = True if location==idx else False
        queue.append([q, flag])
                
    priorities.sort()
    
    answer = 0
    remain = len(priorities)
    while priorities:
        if queue[0][0] == priorities[-1]:
            if queue[0][1]:
                return answer+1
            else:
                queue.popleft()
                priorities.pop()
                answer += 1
                remain -= 1
        else:
            tmp = queue.popleft()
            queue.append(tmp)
            if location:
                location += remain