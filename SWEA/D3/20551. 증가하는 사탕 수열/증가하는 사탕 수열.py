T = int(input())
for tc in range(1,T+1):
    arr= list(map(int, input().split()))
    ans = 0

    for i in range(2,0,-1):
        if arr[i] < 1 or arr[i-1] < 1:
                ans = -1
                break
        if arr[i] <= arr[i-1]:
            t = arr[i-1] - (arr[i]-1)
            
        
            ans += t
            arr[i-1] -= t
            if arr[i-1] < 1:
                ans = -1
                break
    print(f"#{tc} {ans}")