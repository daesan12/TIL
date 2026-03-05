def find_max_h():
    max_h = 0
    for i in range(N):
        if max_h < max(arr[i]):
            max_h = max(arr[i])
    return max_h

def find_start():
    start_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_h:
                start_list.append((i,j))
    return start_list

def dfs(r,c,used,length):
    visited[r][c] = True
    global ans
    ans = max(ans, length)
    for d in range(4):
        nr = r + di[d]
        nc = c + dj[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            h = arr[r][c]
            nh = arr[nr][nc]
            if nh < h:
                visited[nr][nc] =True
                dfs(nr,nc,used,length + 1)
                visited[nr][nc] =False
            elif used == 0 and nh - K < h:
                original = arr[nr][nc]
                arr[nr][nc] = h - 1
                visited[nr][nc] = True
                dfs(nr,nc,1,length + 1)
                visited[nr][nc] = False
                arr[nr][nc] = original
    visited[r][c] = False
    return length
        

di = [0,1,0,-1]
dj = [1,0,-1,0]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]* N for _ in range(N)]
    ans = 0
    s = []
    max_h = find_max_h()
    start_list = find_start()

    for r,c in start_list:
        dfs(r,c,0,1)
       

    print(f"#{tc} {ans}")