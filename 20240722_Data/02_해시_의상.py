# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    info = dict()
    for name, cloth in clothes:
        if not info.get(cloth):
            info[cloth] = list()
        info[cloth].append(name)

    answer = 1
    for cloth, ls in info.items():
        answer *= len(ls)+1
        
    return answer - 1