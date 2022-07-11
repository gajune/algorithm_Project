def solution(id_list, report, k):
    answer = [0] * len(id_list)  # 아이디의 갯수만큼 0이 들어간 리스트 선언
    report = list(set(report))  # 중복제거
    reported = {x: 0 for x in id_list}  # 아이디가 키, 값은 0으로 딕셔너리 선언

    for report_info in report:
        a, b = report_info.split()  # 공백을 기준으로 나눔
        reported[b] += 1  # 신고횟수 1증가

    for report_info in report:
        a, b = report_info.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1  # id_list의 순서대로 신고결과 1증가
    return answer
