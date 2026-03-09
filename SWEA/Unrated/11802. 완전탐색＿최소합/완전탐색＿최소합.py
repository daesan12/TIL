T = int(input())

def find_min(r,c,cost):
    global min_sum
    visited[r][c] = cost
    if r == N-1 and c == N-1:
        min_sum = min(min_sum,visited[r][c])
        return
    for i in range(2):
        nr = r + di[i]
        nc = c + dj[i]
        if 0 <= nr < N and 0 <= nc < N:
            if visited[r][c] + arr[nr][nc]> visited[nr][nc]:
                continue 
            find_min(nr,nc,cost+arr[nr][nc])

#우,하
di = [1,0]
dj = [0,1]
for tc in range(1,T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    visited = [[9999] * N for _ in range(N)]
    min_sum = 999999999
    find_min(0,0,arr[0][0])
    print(f"#{tc} {visited[N-1][N-1]}")
