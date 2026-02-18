N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]  # [방향, 길이]

# 1) 큰 가로(W) / 큰 세로(H) 및 인덱스 찾기
W = -1
H = -1
W_idx = -1
H_idx = -1

for i in range(6):
    d, L = arr[i]
    if d in (1, 2):  # 가로
        if L > W:
            W = L
            W_idx = i
    else:            # 세로 (3,4)
        if L > H:
            H = L
            H_idx = i

# 2) 구멍(작은 직사각형) 변 길이 = "최댓값 변의 양옆 길이 차이"
h = abs(arr[(W_idx - 1) % 6][1] - arr[(W_idx + 1) % 6][1])  # 구멍 세로
w = abs(arr[(H_idx - 1) % 6][1] - arr[(H_idx + 1) % 6][1])  # 구멍 가로

# 3) 넓이 = 큰 사각형 - 작은 사각형, 그리고 N(참외 수/면적당 개수) 곱
area = W * H - w * h
print(area * N)
