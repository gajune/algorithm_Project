# 해시 == 딕셔너리

def solution(participant, completion):
    answer = ''
    name = {x: 0 for x in set(participant)}
    for part in participant:
        if part in name:
            name[part] += 1
    for part in completion:
        if part in name:
            name[part] -= 1
    for part in name:
        if name[part] == 1:
            answer = part
            break
    return answer
