def solution(info, edges):
    visited = [0] * len(info)  # 노드가 지났는지 안지났는지 판단하는 리스트
    visited[0] = 1  # 루트 노드는 무조건 지남
    answer = []  # 양이 늑대보다 많은 경우의 수를 모두 저장할 리스트

    def check_node(sheep, wolf):
        if sheep > wolf:  # 양이 늑대보다 많을 경우
            answer.append(sheep)
        else:  # 양이 늑대보다 작거나 같을 경우 재귀함수 종료
            return

        for i in range(len(edges)):  # 모든 경우의 수 탐색
            parent = edges[i][0]  # 부모노드는 edges 0번쨰 값
            child = edges[i][1]  # 자식노드는 edges 1번쨰 값
            if visited[parent] == 1 and visited[child] == 0:  # 부모 지났고 자식은 안지났을 떄
                visited[child] = 1
                if info[child] == 0:  # info 값이 0이면 양
                    check_node(sheep + 1, wolf)
                else:  # 1이면 늑대
                    check_node(sheep, wolf + 1)
                visited[child] = 0  # 전의 상황으로 되돌리기

    check_node(1, 0)  # 양 1마리 늑대 0마리로 시작
    return max(answer)  # 양이 늑대보다 많은 경우의 수 중에서 가장 큰 값을 가져옴
