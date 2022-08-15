def solution(n, arr1, arr2):
    answer = []
    sol = ''
    for bin1, bin2 in zip(arr1, arr2):
        xor_bin = bin1 | bin2
        for trans in bin(xor_bin)[-n:]:
            if trans == '1':
                sol += '#'
            else:
                sol += ' '
        answer.append(sol)
        sol = ''
    return answer
