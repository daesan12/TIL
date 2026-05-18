TC = int(input())

for _ in range(TC):
    # 빈 줄 방지
    N_line = input()
    while N_line.strip() == b'':
        N_line = input()

    N = int(N_line)
    degree = [0] * (N + 1)

    for _ in range(N - 1):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1

    answer = 0
    for d in degree[1:]:
        if d > 2:
            answer += d - 2

    print(answer)