# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# Q. heapq를 이용했을 때 min_2가 항상 min_2 일 수 있을까?

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    i = 0
    while len(scoville) >= 2:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return i
        else:
            i += 1
            min_2 = heapq.heappop(scoville)
            new = min_1 + min_2*2
            heapq.heappush(scoville, new)
            
    if scoville[0] > K:
        return i
    else:
        return -1