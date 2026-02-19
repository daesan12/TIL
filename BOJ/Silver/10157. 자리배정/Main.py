C,R = map(int,input().split())
N = int(input())
if  C*R < N:
    print(0)
    exit()
    
arr = [[0] * C for _ in range(R)]
row_idx = R-1
col_idx = 0

ans = False
#상우하좌
dcol = [0,1,0,-1]
drow = [-1,0,1,0]
arr[row_idx][col_idx] = 1
go = 0
count = 1
while count <N:
    nrow = row_idx + drow[go]
    ncol = col_idx + dcol[go]
    if not (0<= nrow < R and 0<= ncol < C) or arr[nrow][ncol] != 0:
        go = (go+ 1) % 4
        continue
    row_idx = nrow
    col_idx = ncol
    count +=1
    arr[row_idx][col_idx] = count
    if count == N:
        break
x = col_idx + 1
y = R - row_idx
print(x, y)
