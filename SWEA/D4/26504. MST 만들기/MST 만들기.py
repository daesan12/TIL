TC = int(input())

for _ in range(TC):
    N = int(input())
    M = N * (N - 1) // 2

    arr = list(map(int, input().split()))
    arr.sort()

    min_cost = sum(arr[:N - 1])

    max_cost = 0
    idx = 0

    for i in range(N - 1):
        max_cost += arr[idx]
        idx += i + 1

    print(min_cost, max_cost)