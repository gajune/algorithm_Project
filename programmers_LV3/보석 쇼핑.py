def solution(gems):
    len_gems = len(gems)
    answer = [0, len_gems]
    kind_gems = len(set(gems))
    start, end = 0, 0
    dic = {gems[0]: 1}
    while start < len_gems and end < len_gems:
        if len(dic) == kind_gems:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == len_gems:
                break
            if gems[end] not in dic:
                dic[gems[end]] = 1
            else:
                dic[gems[end]] += 1

    return [answer[0] + 1, answer[1] + 1]


solution(["DIA", "EM", "EM", "RUB", "DIA"])
