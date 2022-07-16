def solution(a, b):
    answer = 0
    l = len(a)
    num = 0
    while num < l:
        answer += a[num] * b[num]
        num += 1
    return answer
