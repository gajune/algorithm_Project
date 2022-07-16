def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    gym_suit = {x: 1 for x in range(1, n + 1)}
    for lost_student in lost:
        gym_suit[lost_student] -= 1
    for redundancy in reserve:
        gym_suit[redundancy] += 1
    for num in range(1, n + 1):
        if gym_suit[num] > 1:
            if num == 1 and gym_suit[num + 1] < 1:
                gym_suit[num] -= 1
                gym_suit[num + 1] += 1
            elif 1 < num < n:
                if gym_suit[num - 1] < 1:
                    gym_suit[num] -= 1
                    gym_suit[num - 1] += 1
                elif gym_suit[num + 1] < 1:
                    gym_suit[num] -= 1
                    gym_suit[num + 1] += 1
            elif num == n and gym_suit[n - 1] < 1:
                gym_suit[num] -= 1
                gym_suit[num - 1] += 1
    for num in range(1, n + 1):
        if gym_suit[num] > 0:
            answer += 1
    return answer