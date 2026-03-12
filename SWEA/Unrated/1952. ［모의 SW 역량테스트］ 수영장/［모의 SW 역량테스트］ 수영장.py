def dfs(month,price):
    global ans
    if price >= ans:
        return
    if month > 11:
        ans = min (ans,price)
        return
    if month_use[month] == 0:
        dfs(month +1, price)
    
    dfs(month+1, price + (price_list[0]*month_use[month]))#하루
    dfs(month+1, price + price_list[1])#한달
    dfs(month+3, price + price_list[2])#세달

T = int(input())
for tc in range(1,T+1):

    price_list = list(map(int, input().split()))
    month_use = list(map(int, input().split()))
    ans = price_list[3]#연간 이용권으로 고정
    dfs(0,0)
    
    print(f"#{tc} {ans}")