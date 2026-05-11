T = int(input())

for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    answer = 0

    for x, y in points:
        max_width = 0
        max_height = 0

        for nx, ny in points:
            if ny == y:
                max_width = max(max_width, abs(nx - x))


        for nx, ny in points:
            if nx == x:
                max_height = max(max_height, abs(ny - y))

        answer = max(answer, max_width * max_height)

    print(answer)