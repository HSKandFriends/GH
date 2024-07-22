# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    ls = list()
    
    for tmp in s:
        if tmp == '(':
            ls.append(tmp)
        else:
            if len(ls) != 0:
                ls.pop()
            else:
                return False
    if len(ls) == 0:
        return True
    return False