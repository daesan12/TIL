from collections import deque
def bfs(N):
    global answer
    global K
    q = deque()
    q.append((N,0))

    
    while q:
        start,count = q.popleft()
        

        if start == K:
            return count
        
        if 0<=start-1<100001 and visited[start-1]== False:
            q.append((start-1,count +1))
            visited[start-1] =True

        if 0<=start+1<100001 and visited[start+1]== False:
            q.append((start+1,count +1))
            visited[start+1] =True

        if  0<=start*2<100001 and visited[start*2]== False:
            q.append((start*2,count +1))
            visited[start*2] =True

N,K = map(int, input().split())
answer = float('inf')
visited = [False]* 100001
answer = bfs(N)
print(answer)