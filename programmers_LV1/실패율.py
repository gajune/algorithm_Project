def solution(N, stages):
    stages_len = len(stages)
    result = {}
    for stage in range(1, N + 1):
        if stages_len != 0:
            result[stage] = stages.count(stage) / stages_len
            stages_len -= stages.count(stage)
        else:
            result[stage] = 0

    return sorted(result, key=lambda stage: result[stage], reverse=True)
