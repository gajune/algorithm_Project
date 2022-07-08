def solution(numbers, hand):
    answer = ''
    field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    left_x = 3
    left_y = 0
    right_x = 3
    right_y = 2
    num_x = 0
    num_y = 1
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            if num == 1:
                left_x = 0
                left_y = 0
            elif num == 4:
                left_x = 1
                left_y = 0
            else:
                left_x = 2
                left_y = 0
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            if num == 3:
                right_x = 0
                right_y = 2
            elif num == 6:
                right_x = 1
                right_y = 2
            else:
                right_x = 2
                right_y = 2
        else:
            for b in field:
                try:
                    b.index(str(num))
                except ValueError:
                    num_x += 1
                    continue
                else:
                    break
            if abs(right_x - num_x) + abs(right_y - num_y) > abs(left_x - num_x) + abs(left_y - num_y):
                answer += 'L'
                left_x = num_x
                left_y = num_y
            elif abs(right_x - num_x) + abs(right_y - num_y) < abs(left_x - num_x) + abs(left_y - num_y):
                answer += 'R'
                right_x = num_x
                right_y = num_y
            else:
                if hand == 'right':
                    answer += 'R'
                    right_x = num_x
                    right_y = num_y
                else:
                    answer += 'L'
                    left_x = num_x
                    left_y = num_y
        num_x = 0
    return answer
