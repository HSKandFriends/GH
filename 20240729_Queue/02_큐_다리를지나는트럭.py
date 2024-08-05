# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length:int, weight:int, truck_weights:list):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights.reverse()
    
    sum_weights = 0
    
    while truck_weights:
        answer += 1
        sum_weights -= bridge.popleft()
        truck = truck_weights[-1]
        
        if sum_weights+truck <= weight:
            truck_weights.pop()
            bridge.append(truck)
            sum_weights += truck
        else:
            bridge.append(0)
            
    return answer+bridge_length