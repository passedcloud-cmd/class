#####################################################################################
# 그래프 구현 연습############################################################################
#####################################################################################

# # 7 8
# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


# V, E = 7, 8
# txt = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
# data = list(map(int, txt.split()))

# # 인접 행렬 만들기 - 간선으로 이어진 좌표를 1로 설정
# # 0으로 채워진 (V+1) X (V+1) 행렬 만들기
# adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# # 간선 수 만큼 반복해서 연결 여부를 정하기
# for i in range(E):
#     node1, node2 = data[i * 2], data[i * 2 + 1]
#     adj_matrix[node1][node2] = 1
#     # 무향이니까 대각선을 기준으로 대칭
#     adj_matrix[node2][node1] = 1

# print("\n인접 행렬")
# for row in adj_matrix:
#     print(row)


# # 인접 리스트 만들기 -  1번 노드와 이어진 노드들은 1번 리스트에 넣기. 2번 노드와 이어진 노드들은 2번 리스트에...
# # 빈 리스트로 채워진 (V + 1) x (V + 1) 행렬 만들기
# adj_list = [[] * (V + 1) for _ in range(V + 1)]

# # 간선 E 개수만큼 반복
# for i in range(E):
#     node1, node2 = data[i * 2], data[i * 2 + 1]
#     adj_list[node1].append(node2)
#     # 무향이니까 adj_list[node2]에도 node1 추가
#     adj_list[node2].append(node1)

# print("\n인접 리스트")
# print(adj_list)
# for i in range(1, V + 1):
#     print(f'노드{i}: {adj_list[i]}')





#####################################################################################
# DFS 연습############################################################################
#####################################################################################
# input 
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# output
# 1246573



# 재귀 방식1 - 인접 리스트 + 재귀
def dfs_recursive_list(current_node, adj_list, visited, path):
    # 1. 현재 노드 방문 처리
    visited[current_node] = True
    path.append(current_node)

    # 2. 현재 노드와 연결된 인접 노드들을 직접 순회
    # 인접 행렬처럼 모든 노드를 확인할 필요 없이, 연결된 노드만 바로 탐색
    for next_node in adj_list[current_node]:
        # 인접 노드에 아직 방문하지 않았다면 재귀 호출
        if not visited[next_node]: # 전부 방문하면 재귀 종료됨
            dfs_recursive_list(next_node, adj_list,visited, path)

# 리스트로 그래프 구성
V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    node1, node2 = data[i * 2], data[i * 2 + 1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
print(f'인접리스트: {adj_list}')
# DFS 실행
visited = [False] * (V + 1) # 0번째 인덱스는 비워두기
traversal_path = []
dfs_recursive_list(1, adj_list, visited, traversal_path) # 시작 노드가 1이라고 명시됨
print(f'인접리스트+재귀 방식:\n{traversal_path}')
print(''.join(map(str, traversal_path)))



############################################################################################
# 재귀 방식2 - 인접 행렬 + 재귀
print('\n')
def dfs_recursive_matrix(current_node, adj_matrix, visited, path):
    # 1. 현재 노드 방문 처리
    visited[current_node] = True
    path.append(current_node) 

    # 2. 현재 노드와 연결된 다른 노드들을 순회
    # V는 adj_matrix의 크기로 알 수 있으므로, 전역 변수 V에 의존하지 않아도 됨
    #len(adj_matrix) = V + 1
    for next_node in range(1, len(adj_matrix)): 
        if adj_matrix[current_node][next_node] and not visited[next_node]:
            dfs_recursive_matrix(next_node, adj_matrix, visited, path)

# 인접행렬로 그래프 구성
V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))

adj_matrix = [[0] * (V + 1) for _ in range(V+1)]

for i in range(E):
    node1, node2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[node1][node2] = 1
    adj_matrix[node2][node1] = 1

# DFS 실행
visited = [False] * (V + 1)
traversal_path = []

dfs_recursive_matrix(1, adj_matrix, visited, traversal_path)
result = ''.join(map(str, traversal_path))
print(f'인접행렬+재귀방식:\n{result}')


################################################################################################
# 스택 방식1 - 인접 리스트 + 스택 - pop 시점 방문 처리
# 스택에 다 넣고 난 다음 pop해서 방문 여부 확인 - 같은 노드가 stack에 여러 번 들어갈 수 있음
print("\n")
def dfs_stack_pop_style(start):
    """pop 후에 방문 처리"""
    visited = [False] * (V + 1) # 방문 여부 리스트
    stack = [start] # 시작 노드를 스택에 넣고 시작
    path = [] # 탐색 경로 저장

    while stack:
        # 스택의 가장 위에서 노드를 하나 꺼냄
        current_node = stack.pop()

        # 이 노드를 방문한 적 있는지 꺼낸 후에 확인
        if not visited[current_node]:
            # 방문한 적이 없으면, 방문 처리
            visited[current_node] = True
            path.append(current_node)

            # 현재 노드와 연결된 인접 노드들을 스택에 추가
            # 이미 방문 처리된 노드라도 스택에 들어갈 수 있지만,
            # 위 if 문에서 걸러지므로 탐색 순서에는 영향을 주지 않음
            for next_node in adj_list[current_node]:
                if not visited[next_node]:
                    stack.append(next_node)
    return path

V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))

adj_list = [[] for _ in range(V + 1)]


for i in range(E):
    node1, node2 = data[2 * i], data[i * 2 + 1]
    adj_list[node1].append(node2) 
    adj_list[node2].append(node1)


# 방문 순서를 결정하기 위해 인접 리스트를 각 노드별로 내림차순 정렬
# 내림차순 정렬해두면, 스택에서 pop할 때 작은 번호를 먼저 방문하도록 유도 가능
# 문제의 요구사항(노드를 작은 번호부터 방문해야 한다)과 스택의 LIFO 구조를 맞추기 위함
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)

print(f'인접리스트: {adj_list}')

# DFS 실행
result_path = dfs_stack_pop_style(1)
print(f'인접리스트+스택 방식:')
print(''.join(map(str, result_path)))



################################################################################################
# 스택 방식2 - 인접 리스트 + 스택 - push 시점 방문 처리
# 방문 여부를 확인하고 stack에 넣음 - 같은 노드는 stack에 최대 1번만 들어감 
print('\n')
def dfs_stack_push_style(start_node):
    visited = [False] * (V + 1)
    stack = []
    path = []

    # 1. 시작 노드를 먼저 방문 처리하고 스택에 push
    visited[start_node] = True
    stack.append(start_node)

    while stack:
        # 2. 스택에서 노드를 pop하여 경로에 추가
        current_node = stack.pop()
        path.append(current_node)

        # 3. 현재 노드의 인접 노드들을 확인
        # adj_list가 내림차순 정렬되어 있으므로 큰 번호부터 확인
        for next_node in adj_list[current_node]:
            # 방문한 적 없으면
            if not visited[next_node]:
                # 방문 처리(예약)하고 스택에 push
                visited[next_node] = True
                stack.append(next_node)

    return path
result = ''.join(map(str, dfs_stack_push_style(1)))
print(f'인접 리스트 + 스택 - push 시점 방문 처리\n{result}')




print('\n연습')


V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))

adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = data[i*2], data[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

def list_pop_dfs(start):
    visited = [False] * (V+1)
    path = []
    stack = []
    stack.append(start)

    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True
            path.append(current_node)

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                stack.append(next_node)

    return path

result = list_pop_dfs(1)
print(f'pop{result}')    




V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))

adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = data[i*2], data[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

def list_push_dfs(start):
    visited = [False] * (V+1)
    path = []
    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        current_node = stack.pop()
        path.append(current_node)

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

    return path

result = list_push_dfs(1)
print(f'push{result}')