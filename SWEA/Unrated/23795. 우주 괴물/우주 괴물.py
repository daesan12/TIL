T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for k in range(4):
                    for step in range(1,N):
                        ni = i + di[k] * step
                        nj = j + dj[k] * step
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] != 0:
                                break
                            else:
                                arr[ni][nj] = -1
                break
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count +=1
    print(f"#{tc} {count}")