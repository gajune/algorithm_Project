def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    answer = []

    for num in range(len(answers)):
        if answers[num] == s1[num % len(s1)]:  # 리스트 안에 있는 숫자가 반복되는 상황이므로 나머지 연산자 사용
            c1 += 1
        if answers[num] == s2[num % len(s2)]:
            c2 += 1
        if answers[num] == s3[num % len(s3)]:
            c3 += 1
    temp = [c1, c2, c3]
    for student, check in enumerate(temp):  # enumerate() 인덱스와 값을 리턴
        if check == max(temp):
            answer.append(student + 1)
    answer.sort()
    return answer
