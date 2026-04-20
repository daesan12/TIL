import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_v = -10**18
min_v = 10**18

def dfs(idx, current, plus, minus, mul, div):
    global max_v, min_v

    if idx == N:
        max_v = max(max_v, current)
        min_v = min(min_v, current)
        return

    if plus:
        dfs(idx + 1, current + nums[idx], plus - 1, minus, mul, div)

    if minus:
        dfs(idx + 1, current - nums[idx], plus, minus - 1, mul, div)

    if mul:
        dfs(idx + 1, current * nums[idx], plus, minus, mul - 1, div)

    if div:
        if current < 0:
            dfs(idx + 1, -((-current) // nums[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, current // nums[idx], plus, minus, mul, div - 1)

dfs(1, nums[0], plus, minus, mul, div)

print(max_v)
print(min_v)