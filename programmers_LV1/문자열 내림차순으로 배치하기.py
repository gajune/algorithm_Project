def solution(s):
    s = sorted(s, reverse=True)
    answer = ''
    for alp in s:
        answer += alp
    return answer
