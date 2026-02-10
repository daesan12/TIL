T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, (input().split())) #V= 노드의 수 E =간선의 수
    G = [[] for _ in range(V + 1)]#간선의 수 +1 만큼 2차원배열만들기 각 수가 각index에 들어가야하기때문

    for _ in range(E):
        u, v = map(int, input().split()) #u노드에서 -> v노드로의 간선을 표시
        G[u].append(v)#u번 인덱스에 v를 입력, 각 간선의 인접 노드를 저장

    start, end = map(int, input().split())#시작노드 , 끝 노드 입력
    visited = [0] * (V + 1)#방문 여부를 저장하는 리스트 생성 노드의 수 +1,노드의 숫자범위가 1부터 시작하기때문

    S = []#인접 노드가 모드 방문한 상태일때 어떤노드로 돌아와야할지 저장하는 스택선언

    visited[start] = 1 #스타트 노드를 방문표시
    v = start #v 를 스타트 노드의 번호로 지정

    while True: #무조건 실행
        for w in G[v]:#v번 노드의 인접 노드를 순회
            if not visited[w]:#w(v)번의 노드가 방문하지않은 상태(0)라면 실행
                visited[w] = 1 #w(v)번의 노드를 방문한 상태(1)로 변환
                S.append(v) #스택에 (현재노드)v번의 노드를 추가(돌아갈 지점 저장)
                v = w #다음 탐색할노드로 변경
                break #for문 종료
        else:#break문을 만나지 않았을떄 실행== G[v]==비어있을때
            if S:#스택에 값이 있다면
                v = S.pop() #S 스택을 pop하여 v에 저장하여 v 노드로 다시 돌아감
            else:#스택이 값이없다면
                break#최상단으로 돌아왔다는 뜻이기 때문에 종료
    print(f"#{tc} {visited[end]}")
