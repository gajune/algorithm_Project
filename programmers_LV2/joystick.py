def solution(name):
    answer = 0
    cursor = 0
    for num, al in enumerate(name):
        if al == 'A':
            continue
        else:
            if abs(cursor - num) > abs(len(name) + cursor - num):
                answer += abs(len(name) + cursor - num)
            elif abs(cursor - num) < abs(len(name) + cursor - num):
                answer += abs(cursor - num)
            else:
                answer += abs(cursor - num)
            if ord(al) <= 78:
                answer += ord(al) - 65
            else:
                answer += 91 - ord(al)
            cursor = num
    return answer
print(solution("BBBBAAAABA"))