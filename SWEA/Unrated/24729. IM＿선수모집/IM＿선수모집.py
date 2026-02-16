T = int(input())

for test_case in range(1, T + 1):
    N, K= map(int,(input().split()))
    arr = list(map(int, input().split()))
   
    max_count = 0
    
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i]-K <= arr[j] and arr[i] > arr[j]-K:
                count += 1
        if max_count < count:
            max_count = count

    print(f"#{test_case} {max_count}")