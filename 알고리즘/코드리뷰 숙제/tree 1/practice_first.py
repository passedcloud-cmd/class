# 완전 이진 트리 - 1차원 배열의 인덱스 규칙 활용
# 1. 입력 받기
N = 6
raw_data = ['A', 'B', 'C', 'D', 'E', 'F']

# 2. 트리 저장소 만들기 - 1차원 배열
# 0번 인덱스는 비워두고 1번 인덱스부터 채우기
tree = [0] + raw_data

# tree 리스트 상태: [0, 'A', 'B', 'C', 'D', 'E', 'F']
# 인덱스(i)      :  0   1    2    3    4    5    6

# 3. 인덱스 규칙으로 부모/자식 찾기 함수 만들기
def get_children(idx):
    """
    인덱스 idx를 입력 받으면 왼쪽 자식과 오른쪽 자식을 출력
    배열 범위를 벗어나면 자식이 없는 것
    """
    # 범위 벗어남
    if idx >= len(tree):
        return

    # 왼쪽 자식 찾기 (idx * 2)
    left_idx = idx * 2
    if left_idx < len(tree):
        print(f"{idx}의 왼쪽 자식 : {tree[left_idx]}, 인덱스 : {left_idx}")
    # 범위 벗어나면
    else:
        print(f"{idx} 왼쪽 자식 없음")

    # 오른쪽 자식 찾기 (idx * 2 + 1)
    right_idx = idx * 2 + 1
    if right_idx < len(tree):
        print(f"{idx}의 오른쪽 자식 : {tree[right_idx]}, 인덱스 : {left_idx}")
    # 범위 벗어나면
    else:
        print(f"{idx} 오른쪽 자식 없음")


get_children(3)





# 일반 이진 트리 - 연결 리스트 ( 자식 배열 ) 활용
# 누가 누구의 자식인지 명시적으로 저장하는 배열리스트 사용

# 1. 정보 입력
# V는 노드의 총 개수
V = 13
# E는 엣지의 총 개수
E = V - 1
# 간선 정보 리스트
edge = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 2. 트리 저장소 만들기
# 노드 번호가 1번부터 시작하니까 V + 1 크기로 생성
left = [0] * (V + 1)
right = [0] * (V + 1)

# 3. 간선 정보 순회하며 트리 채우기
for i in range(E):
    parent = edge[i * 2]
    child = edge[i * 2 + 1]

    # 왼쪽이 비었으면 왼쪽 자식
    if left[parent] == 0:
        left[parent] = child
    # 왼쪽이 안 비었으면 오른쪽 자식
    else:
        right[parent] = child

print(f'왼쪽 자식: {left}'"\n" f'오른쪽 자식: {right}')




# 순회를 하려면 이 left와 right 리스트가 있어야 함
# 순회 이전에 위쪽 작업을 해야 함

# 전위 순회(preorder Traversal) VLR
def preorder(node):
    # 기저 조건: 유효하지 않은 노드(0)이면 바로 빠져나간다
    if node == 0:
        return

    # 1. 나(Visit) 머저 처리
    print(node, end=' ')
    # 2. 왼쪽 자식으로 이동
    preorder(left[node])
    # 3. 오른쪽 자식으로 이동
    preorder(right[node])

preorder(1)


