def solution(lottos, win_nums):
    answer = []
    best_rank = 1
    worst_rank = 1
    for check in lottos:
        if check != 0:
            try:
                win_nums.index(check)
            except ValueError:
                if best_rank < 6:
                    best_rank += 1
                if worst_rank < 6:
                    worst_rank += 1
        else:
            if worst_rank < 6:
                worst_rank += 1
    answer.append(best_rank)
    answer.append(worst_rank)
    return answer
