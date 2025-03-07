# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution_(progresses, speeds):
    length = len(progresses)
    success = 0
    answer = []
    while True:
        for i in range(success, length):
            progresses[i] += speeds[i]

        if success == length:
            break
        elif success+1 == length:
            answer.append(1)
            break
        
        if progresses[success] >= 100:
            cnt = 1
            while progresses[success+cnt] >= 100:
                cnt += 1
                if success+cnt == length:
                    break
            answer.append(cnt)
            success += cnt

    return answer

def solution(progresses:list, speeds:list):
    answer = list()
    time = 0
    success = 0
    
    while progresses:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            success += 1
        else:
            if success > 0:
                answer.append(success)
                success = 0
            time += 1
    
    answer.append(success)
    
    return answer