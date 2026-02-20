T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 최소 힙 (1번 인덱스부터 사용)
    heap = [0] * (N + 1)
    last = 0

    # 힙에 삽입
    for num in nums:
        last += 1
        heap[last] = num
        child = last
        parent = child // 2

        # heapify-up
        while parent >= 1 and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2
    # 마지막 노드의 조상 합 구하기
    result = 0
    idx = last // 2  # 부모부터 시작

    while idx >= 1:
        result += heap[idx]
        idx //= 2

    print(f"#{tc} {result}")