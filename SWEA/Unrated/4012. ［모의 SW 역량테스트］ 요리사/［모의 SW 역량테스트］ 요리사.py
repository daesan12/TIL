
# 음식 하나의 맛을 계산하는 함수
def get_taste(food, arr):
    total = 0

    # food 안의 재료들 중에서 2개씩 뽑는 모든 조합을 확인
    # 예: food = [0,2,3] 이면
    # (0,2), (0,3), (2,3) 이렇게 계산
    for i in range(len(food)):
        for j in range(i + 1, len(food)):
            a = food[i]
            b = food[j]

            # 문제에서 시너지는 S[a][b] + S[b][a] 둘 다 더해야 함
            total += arr[a][b] + arr[b][a]

    return total


# A음식에 들어갈 재료를 조합으로 고르는 DFS
def dfs(idx, start):
    global ans

    # 재료를 N/2개 골랐으면
    if idx == N // 2:
        food_a = []
        food_b = []

        # selected[i] == True  -> A 음식
        # selected[i] == False -> B 음식
        for i in range(N):
            if selected[i]:
                food_a.append(i)
            else:
                food_b.append(i)

        # 두 음식의 맛 계산
        taste_a = get_taste(food_a, arr)
        taste_b = get_taste(food_b, arr)

        # 맛 차이의 최솟값 갱신
        ans = min(ans, abs(taste_a - taste_b))
        return

    # 조합 생성
    for i in range(start, N):
        selected[i] = True
        dfs(idx + 1, i + 1)
        selected[i] = False


T = int(input())
# selected로 A음식 재료를 고르고
# 남은 걸 B로 만들고
# 두 음식 맛 차이를 계산하고
# 다시 원상복구하면서 모든 조합을 탐색
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans = float('inf')
    # selected[i] == True 면 A음식에 넣은 재료
    selected = [False] * N
    # 중복 경우를 줄이기 위해 0번 재료는 무조건 A에 넣고 시작
    # 예를 들어
    # A={0,1}, B={2,3}
    # A={2,3}, B={0,1}
    # 는 사실 같은 경우라서 반만 보기 위해 이렇게 함
    selected[0] = True
    dfs(1, 1)

    print(f"#{tc} {ans}")