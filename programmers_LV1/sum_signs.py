def solution(absolutes, signs):
    num = 0
    for sign in signs:
        if not sign:
            absolutes[num] = -absolutes[num]
        num += 1
    answer = sum(absolutes)
    return answer
