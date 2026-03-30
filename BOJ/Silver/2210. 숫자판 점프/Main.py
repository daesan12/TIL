arr = [list(input().split()) for _ in range(5)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
def dfs(i,j,str,dep):
    if dep == 6:
        t.append(str)
        return
    

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni,nj,str+arr[ni][nj],dep+1)
    return

t = []
for i in range(5):
    for j in range(5):
        dfs(i,j,'',0)
print(len(set(t)))