N = int(input())
arr = list(map(int, input().split()))
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    if students[i][0]==1:
        for j in range(students[i][1]-1,N,students[i][1]):
            arr[j] ^= 1
    elif students[i][0] == 2:
        a = students[i][1] -1
        b = students[i][1] -1 
        arr[a] ^= 1
        while True:
            a -= 1
            b += 1
            if 0 <= a and b < N:
                if arr[a] == arr[b]:
                    arr[a] ^= 1
                    arr[b] ^= 1
                else:
                    break
            else:
                break
for i in range(N):
    print(arr[i], end = " ")
    if (i+1)% 20 == 0:
        print()