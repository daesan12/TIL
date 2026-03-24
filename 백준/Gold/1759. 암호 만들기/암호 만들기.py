def dfs(start,path):
    if len(path) == L:
        vowel = 0
        consonant = 0
        for i in path:
            if i in "aeiou":
               vowel += 1
            else:
               consonant += 1
        if vowel >= 1 and consonant >= 2:
            print(path)
            return
        return

    for i in range(start,C):

        dfs(i+1,path + arr[i])
#L=만 들어야하는 문자열길이 C=주어진 글자 수
L,C = map(int, input().split())
arr = list(input().split())

arr.sort()
dfs(0,'')