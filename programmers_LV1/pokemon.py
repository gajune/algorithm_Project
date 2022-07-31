def solution(nums):
    nums_len = len(nums)
    nums = set(nums)
    answer = 0
    for num in nums:
        if answer < nums_len / 2:
            answer += 1
    return answer
