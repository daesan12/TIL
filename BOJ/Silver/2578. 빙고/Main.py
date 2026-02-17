#가로세로
def is_binggo():
    binggo = 0
    for i in range(5):
        if binggo >= 3:
            return True
        if arr[i].count(0) == 5:
            binggo += 1
        for j in range(5):
            if binggo >= 3:
                return True
            if arr[j][i] != 0:
                break
        else:
            binggo += 1
    #왼쪽위시작 대각선
    for i in range(5):
        if arr[i][i] != 0:
            break
    else:
        binggo += 1
        if binggo >= 3:
            return True
        
    #왼쪽아래시작 대각선
    eorkr = 0
    for i in range(4,-1,-1):
        
        if arr[i][eorkr] != 0:
            break
        eorkr += 1
    else:
        binggo += 1
        if binggo >= 3:
                return True
    return False   

arr = [list(map(int, input().split())) for _ in range(5)]
binggo_arr = [list(map(int, input().split())) for _ in range(5)]

count = 0
binggo = False
for i in range(5):
    for j in range(5):
        count += 1
        for k in range(5):
            for l in range(5):
                if arr[k][l] == binggo_arr[i][j]:
                    arr[k][l] = 0
                    if is_binggo():
                        print(count)
                        binggo = True
                        break
            if binggo:
                break
        if binggo:
            break
    if binggo:
        break