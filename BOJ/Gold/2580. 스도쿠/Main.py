def check(r,c,num):
    #가로
    for i in range(9):
        if arr[r][i] == num:
            return False
    #세로
    for i in range(9):
        if arr[i][c] == num:
            return False
    #3X3검증
    sr = (r // 3) * 3
    sc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[sr+i][sc+j] == num:
                return False
            
    #존재하지않는 숫자면 True 반환
    return True
def dfs(idx):
    
    if len(blank) == idx:
        for i in range(9):
            print(*arr[i])
        return True
    
    row,col = blank[idx]

    for num in range(1,10):
        if check(row,col,num):    
            arr[row][col] = num
            if dfs(idx+1) == True:
                return True
            arr[row][col] = 0
    return False

arr = [list(map(int,input().split())) for _ in range(9)]
#빈칸의 좌표를 담을 리스트
blank = []
#빈칸 좌표에 담기
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))
dfs(0)
