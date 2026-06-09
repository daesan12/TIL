di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    i, j = 0, 0
    d = 0

    for num in range(1, N * N + 1):
        arr[i][j] = num

        ni = i + di[d]
        nj = j + dj[d]

        if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] != 0:
            d = (d + 1) % 4
            ni = i + di[d]
            nj = j + dj[d]

        i, j = ni, nj

    print(f'#{tc}')
    for row in arr:
        print(*row)