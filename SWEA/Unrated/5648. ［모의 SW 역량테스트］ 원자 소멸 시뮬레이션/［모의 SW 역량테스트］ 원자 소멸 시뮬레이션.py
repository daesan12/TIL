# 테스트 케이스 개수
T = int(input())

# 방향 벡터
# 문제 기준:
# 0: 상 / 1: 하 / 2: 좌 / 3: 우

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for tc in range(1, T + 1):

    # 원자 개수
    N = int(input())

    # 원자 정보 저장 리스트
    atoms = []

    # 입력 받기
    for _ in range(N):

        x, y, d, k = map(int, input().split())

        # 좌표를 2배 하는 이유
        # 0.5초 충돌 처리 때문
        # ex) (0,0) 과 (1,0)이 만나면
        # 실제론 0.5초 뒤 충돌
        # -> 좌표를 2배하면 1칸 이동으로 표현 가능

        atoms.append([x * 2, y * 2, d, k])

    # 정답(방출된 총 에너지)
    answer = 0

    # 최대 이동 범위만큼 반복
    # 좌표 범위가 최대 2000 * 2 이므로
    # 충분히 큰 값 사용
    for _ in range(4001):

        # 위치별 원자 저장용 dict
        # key   : (x,y)
        # value : 해당 위치 원자들 리스트
        positions = {}

        # -----------------------------
        # 1. 원자 이동
        # -----------------------------
        for atom in atoms:

            x, y, d, k = atom

            # 방향에 따라 이동
            x += dx[d]
            y += dy[d]

            # 이동한 좌표 갱신
            atom[0] = x
            atom[1] = y

            # 현재 위치
            pos = (x, y)

            # 처음 등장한 위치면 빈 리스트 생성
            if pos not in positions:
                positions[pos] = []

            # 해당 위치에 현재 원자 추가
            positions[pos].append(atom)

        # 살아남은 원자 저장 리스트
        new_atoms = []

        # -----------------------------
        # 2. 충돌 처리
        # -----------------------------
        for pos in positions:

            # 현재 위치의 원자들
            same_pos_atoms = positions[pos]

            # 2개 이상이면 충돌
            if len(same_pos_atoms) >= 2:

                # 에너지 합산
                for atom in same_pos_atoms:
                    answer += atom[3]

            # 1개면 생존
            else:
                new_atoms.append(same_pos_atoms[0])

        # 생존 원자로 갱신
        atoms = new_atoms

    # 출력
    print(f'#{tc} {answer}')