answer = 1


def solution(priorities, location):
    global answer
    a = 0
    pri_len = len(priorities)
    while a < pri_len:
        if priorities[0] < priorities[a]:
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            priorities.append(priorities[0])
            priorities.pop(0)
            break
        a += 1
    if location == 0 and a == pri_len:
        return answer
    elif a == pri_len:
        priorities.pop(0)
        answer += 1
        return solution(priorities, location - 1)
    else:
        return solution(priorities, location)
