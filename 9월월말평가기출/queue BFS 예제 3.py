import sys
sys.stdin = open("queue BFS 예제 3.txt")

# 그래프 정보
V, E = map(int, input().split())
edge = list(map(int, input().split()))

# 인접 리스트 만들기
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = edge[i*2], edge[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
for i in range(V+1):
    adj_list[i].sort()




# BFS_큐 만들기
from collections import deque
def BFS_que(start_node, V, adj_list):
    visited = [False] * (V+1)
    path = []
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()
        path.append(current_node)

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return path
path = BFS_que(1, V, adj_list)
print(''.join(map(str, path)))


