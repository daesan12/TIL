import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    # 현재 칸이 청소되지 않은 경우 청소
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1

    found = False

    # 반시계 방향으로 4번 확인
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        # 청소되지 않은 빈 칸이면 전진
        if room[nr][nc] == 0:
            r, c = nr, nc
            found = True
            break

    # 주변 4칸 중 청소할 곳이 없는 경우
    if not found:
        back = (d + 2) % 4
        nr = r + dr[back]
        nc = c + dc[back]

        # 뒤가 벽이면 종료
        if room[nr][nc] == 1:
            break

        # 뒤가 벽이 아니면 후진
        r, c = nr, nc

print(count)