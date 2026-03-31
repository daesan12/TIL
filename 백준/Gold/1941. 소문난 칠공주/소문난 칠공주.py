from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(lst):
    visited =[[0] * 5 for _ in range(5)]
    
    d = deque()
    d.append(lst[0])
    cnt = 1
    idx = d[0]
    row = idx // 5
    col = idx % 5
    visited[row][col] = 1
    while d:   
        
        idx = d.pop()
        row = idx // 5
        col = idx % 5
        
        for k in range(4):
            ni = row+di[k]
            nj = col+dj[k]
            if 0 <= ni < 5 and 0<= nj < 5:
                a = ni * 5
                a += nj
                if a in lst:
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        cnt +=1 
                        d.append(a)
    if cnt == 7:
        return True
    return False

def dfs(start,dep,s_cnt,y_cnt):
    global ans

    if y_cnt > 3:
        return
    
    if dep == 7:
        if s_cnt >= 4:
            #BFS로 연결 검사
            if bfs(selected):
                ans += 1
        return
    
    for i in range(start,25):
        row = i // 5
        col = i % 5
        if arr[row][col] == 'S':
            selected.append(i)
            dfs(i+1,dep+1,s_cnt + 1,y_cnt)
            selected.pop()
        else:
            selected.append(i)
            dfs(i+1,dep+1,s_cnt,y_cnt + 1)
            selected.pop()


arr = [list(input()) for _ in range(5)]
ans = 0
selected = []

dfs(0,0,0,0)
print(ans)