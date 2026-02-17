N = int(input())
xyarr = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*1001 for _ in range(1001)]
n = 1
for i in xyarr:
    y = i[0]
    x = i[1]
    y_plus = i[2]
    x_plus = i[3]
    for j in range(y,y+y_plus):
        for k in range(x,x+x_plus):
            arr[j][k] = n
    n += 1

for i in range(1,N+1):
    count = 0
    for j in range(1001):
        for k in range(1001):
            if arr[j][k] == i:
                count += 1
    print(count)