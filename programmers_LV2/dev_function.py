def solution(progresses, speeds):
    answer = []

    while len(progresses):
        num = 0
        check = 0
        while num < len(progresses):
            if progresses[num] < 100:
                progresses[num] += speeds[num]
            num += 1

        while len(progresses):
            if progresses[0] >= 100:
                check += 1
                del progresses[0]
                del speeds[0]
            else:
                break

        if check:
            answer.append(check)
    return answer
