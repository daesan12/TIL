arr = [[0] * 100 for _ in range(100)]
num = [list(map(int,input().split())) for _ in range(4)]

for i in num:
    x_1 = i[0]
    y_1 = i[1]
    x_2 = i[2]
    y_2 = i[3]
    for j in range(y_1,y_2):
        for k in range(x_1,x_2):
            arr[j][k] = 1
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count +=1

print(count)