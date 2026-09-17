import sys
sys.stdin = open('5177.txt')





T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    def enq(n):
        global last
        # 마지막 정점 추가
        last += 1  # 마지막 정점 추가
        heap[last] = n  # 마지막 정점에 추가

        # 최소힙 : 부모 < 자식
        c = last
        p = c // 2
        # 부모가 있고, 부모 > 자식 이면 교환
        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p  # 부모와 부모의 부모를 비교
            p = c // 2


    heap = [0] * (N + 1) # 정점이 N개인 완전 이진 트리
    last = 0 # 마지막 정점 번호

    for x in arr:
        enq(x)

    print(heap)

    ans = 0
    c = last
    while c // 2 > 0:
        c //= 2
        ans += heap[c]

    print(ans)



# 7
# 5
# 65