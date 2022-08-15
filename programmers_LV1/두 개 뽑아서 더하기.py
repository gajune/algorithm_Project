from itertools import combinations


def solution(numbers):
    answer = []
    for number in list(combinations(numbers, 2)):
        answer.append(sum(number))
    answer = list(set(answer))
    return sorted(answer)
