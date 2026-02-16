arr = [int(input()) for _ in range(9)]
 

num = sum(arr) - 100
find = 0
for i in range(9):
    for j in range(i+1,9):
        sum_nan = arr[i]+arr[j]
        if sum_nan == num:
            arr[i] = 0
            arr[j] = 0
            find = 1
            break
    if find == 1:
        break
arr.sort()
for i in range(2,9):
    print(arr[i])
