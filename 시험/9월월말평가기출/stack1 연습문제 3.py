import sys
sys.stdin = open("stack1 연습문제 3.txt")

# 그래프 정보
V, E = map(int, input().split())
edge = list(map(int, input().split()))

# 리스트 만들기
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = edge[i*2], edge[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

# for row in adj_list:
#     print(row)

# # DFS-재귀 함수 만들기
# def dfs_recursive(start_node, visited, path, adj_list):
#     visited[start_node] = True
#     path.append(start_node)
#     for next_node in adj_list[start_node]:
#         if not visited[next_node]:
#             dfs_recursive(next_node, visited, path, adj_list)

# visited = [False] * (V+1)
# path = []
# for i in range(V+1):
#     adj_list[i].sort()

# dfs_recursive(1, visited, path, adj_list)
# result = ''.join(map(str, path))
# print(result)



visited2 = [False] * (V+1)
path = []
for i in range(V+1):
    adj_list[i].sort(reverse=True)
# DFS-스택 함수 만들기
def dfs_stack(start_node):
    stack = []
    stack.append(start_node)
    
    while stack:
        current_node = stack.pop()
        if not visited2[current_node]:
            visited2[current_node] = True
            path.append(current_node)
            for next_node in adj_list[current_node]:
                if not visited2[next_node]:
                    stack.append(next_node)

    return path
dfs_stack(1)
print(''.join(map(str, path)))
