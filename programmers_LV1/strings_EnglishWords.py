def solution(s):
    answer = ''
    check = ''
    a = 0
    number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while a < len(s):
        if s[a].isdigit():
            answer = answer + s[a]
        else:
            check = check + s[a]
            try:
                number_list.index(check)
            except ValueError:
                a += 1
                continue
            else:
                answer = answer + str(number_list.index(check))
                check = ''
        a += 1
    return int(answer)
