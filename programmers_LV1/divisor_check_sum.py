def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        check = 2
        if i == 1:
            check = 1
        for num in range(2, (i // 2) + 1):
            if i % num == 0:
                check += 1
        if check % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
