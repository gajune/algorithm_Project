def solution(array, commands):
    answer = []
    for command in commands:
        sli = array[command[0] - 1: command[1]]
        sli.sort()
        answer.append(sli[command[2] - 1])
    return answer

