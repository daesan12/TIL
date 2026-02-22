n, k = map(int, input().split())

arr = [i for i in range(1,n+1)]
index = 0
while len(arr) != 1:
    index = (index+k-1)%len(arr)
    print(arr[index],end =" ")
    arr.pop(index)
    
print(arr[0])