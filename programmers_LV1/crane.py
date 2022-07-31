def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for doll in board:
            if board[len(board) - 1][move - 1] == 0:
                break
            if doll[move - 1] == 0:
                continue
            basket.append(doll[move - 1])
            doll[move - 1] = 0
            if len(basket) > 1:
                if basket[len(basket) - 1] == basket[len(basket) - 2]:
                    answer += 2
                    del basket[len(basket) - 1]
                    del basket[len(basket) - 1]
            break
    return answer
