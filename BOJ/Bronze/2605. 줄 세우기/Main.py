N = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(N):
    result.insert(i - arr[i],i)

for i in range(N):
    print(result[i]+1)