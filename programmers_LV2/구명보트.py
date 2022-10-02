from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)

    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
        else:
            q.pop()
        answer += 1
    if len(q) == 1:
        answer += 1
    return answer
