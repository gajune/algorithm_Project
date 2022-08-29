def solution(survey, choices):
    answer = ''
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for idx, val in enumerate(survey):
        if choices[idx] < 4:
            score[survey[idx][0]] += 4 - choices[idx]
        else:
            score[survey[idx][1]] += choices[idx] - 4

    if score["R"] >= score["T"]:
        answer += "R"
    else:
        answer += 'T'

    if score["C"] >= score["F"]:
        answer += "C"
    else:
        answer += 'F'

    if score["J"] >= score["M"]:
        answer += "J"
    else:
        answer += 'M'

    if score["A"] >= score["N"]:
        answer += "A"
    else:
        answer += 'N'

    return answer
