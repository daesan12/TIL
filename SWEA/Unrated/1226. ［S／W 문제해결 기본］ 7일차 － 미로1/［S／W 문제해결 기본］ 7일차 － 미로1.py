from collections import deque
def find_start_and(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i,j)
            elif maze[i][j] == 3:
                end = (i,j)
    return start,end



di = [0,1,0,-1]
dj = [1,0,-1,0]



T = 10
for _ in range(T):
    visited = [[0]*16 for _ in range(16)]
    tc = input()
    maze = [list(map(int, input()))for _ in range(16)]
    start,end = find_start_and(maze)
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    result = 0
    while q:

        start_i,start_j  = q.popleft()
        if maze[start_i][start_j] == 3:
            result = 1
            break 

        for i in range(4):
            ni = start_i + di[i]
            nj = start_j + dj[i]
            if 1 <= ni < 15 and 1 <= nj < 15:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = 1

    print(f"#{tc} {result}")