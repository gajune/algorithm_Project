def solution(prices):
    answer = []

    for idx, price in enumerate(prices):
        check = 0
        if idx == len(prices) - 1:
            answer.append(check)
            break
        for num in range(idx + 1, len(prices)):
            check += 1
            if price > prices[num]:
                break
        answer.append(check)
    return answer
