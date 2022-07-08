def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))  # 중복제거
    reported = {x: 0 for x in id_list}

    for report_info in report:
        a, b = report_info.split()
        reported[b] += 1

    for report_info in report:
        a, b = report_info.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1
    return answer
