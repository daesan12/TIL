T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    direction = 0

    for num in range(1, N * N + 1):
        arr[x][y] = num

        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 밖이거나 이미 숫자가 있으면 방향 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny

    print(f'#{tc}')
    for row in arr:
        print(*row)