import sys
input = sys.stdin.readline

n = int(input())
INF = 10**9

# 거리 배열 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신까지 거리는 0
for i in range(1, n + 1):
    dist[i][i] = 0

# 친구 관계 입력
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드-워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 각 회원의 점수 계산
scores = []
for i in range(1, n + 1):
    scores.append(max(dist[i][1:]))

min_score = min(scores)
candidates = []

for i in range(n):
    if scores[i] == min_score:
        candidates.append(i + 1)

print(min_score, len(candidates))
print(*candidates)