def solution(n):
    answer = ''
    for num in range(1, n + 1):
        if num % 2 != 0:
            answer += '수'
        else:
            answer += '박'
    return answer
