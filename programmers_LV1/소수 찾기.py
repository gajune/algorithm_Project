import math


def solution(n):
    answer = 0
    for num in range(2, n + 1):
        tf = True
        for check in range(2, int(math.sqrt(num)) + 1):
            if num % check == 0:
                tf = False
                break
        if tf:
            answer += 1
    return answer
