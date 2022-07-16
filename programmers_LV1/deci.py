import math
from itertools import combinations


def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for num in comb:
        check = True
        for i in range(2, sum(num)):
            if sum(num) % i == 0:
                check = False
                break
        if check:
            answer += 1
    return answer
