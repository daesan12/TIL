T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    s = []
    ans =''
    for i in arr:
        if i in '+-/*':
            if len(s) < 2:
                ans = 'error'
                break
            else:
                a = int(s.pop())
                b = int(s.pop())
                if i == '+':
                    s.append(b + a)
                elif i == '-':
                    s.append(b - a)
                elif i == '*':
                    s.append(b * a)
                elif i == '/':
                    s.append(b // a)
        elif i == '.':
            if len(s) >= 2:
                ans = 'error'
            else:
                ans = s.pop()
        else:
            s.append(i)
    print(f"#{tc} {ans}")