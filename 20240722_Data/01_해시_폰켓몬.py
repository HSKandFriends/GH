# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = int(len(nums)/2)
    pon = set(nums)
    if len(pon) < answer:
        return len(pon)
    return answer