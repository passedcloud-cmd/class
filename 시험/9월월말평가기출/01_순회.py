import sys
sys.stdin = open("01_순회.txt")
V = int(input())
edge = list(map(int, input().split()))

child1 = [0] * (V+1)
child2 = [0] * (V+1)

for i in range(V-1):
    parents = edge[i*2]
    child = edge[i*2+1]
    if child1[parents] == 0:
        child1[parents] = child
    else:
        child2[parents] = child

# print(child1)
# print(child2)

# 전위 순회
def predorder(node):
    if node == 0:
        return 
    print(node, end = ' ')
    predorder(child1[node])
    predorder(child2[node])

print('전위 순회:', end = ' ')
predorder(1)
print()

# 중위 순회
def indorder(node):
    if node == 0:
        return 0

    indorder(child1[node])
    print(node, end = ' ')
    indorder(child2[node])

print('중위 순회:', end = ' ')
indorder(1)
print()

# 후위 순회
def indorder(node):
    if node == 0:
        return 0

    indorder(child1[node])
    indorder(child2[node])
    print(node, end = ' ')

print('후위 순회:', end = ' ')
indorder(1)
print()