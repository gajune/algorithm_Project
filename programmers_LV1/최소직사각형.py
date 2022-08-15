def solution(sizes):
    row = 0
    column = 0
    for size in sizes:
        if row < max(size):
            row = max(size)
        if column < min(size):
            column = min(size)
    return row * column
