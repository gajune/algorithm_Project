def solution(s):
    check = 0
    for bracket in s:
        if check >= 0:
            if bracket == '(':
                check += 1
            else:
                check -= 1
        else:
            return False
    if check == 0:
        return True
    else:
        return False