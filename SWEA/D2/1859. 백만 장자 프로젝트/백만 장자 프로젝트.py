T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 보면서 미래의 최고 판매가를 찾음
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f'#{tc} {profit}')