string = input()
s= []
result = 0
for ch in string:
    if ch == '(' or ch =='[':
        s.append(ch)
    elif  ch == ')':
        temp = 0
        while s and isinstance(s[-1],int):
            temp += s.pop()
        if not s or s[-1] != '(':
            print(0)
            exit()
        s.pop()
        if temp == 0:
            s.append(2)
        else:
            s.append(temp * 2)
    elif ch == ']':
        temp = 0
        while s and isinstance(s[-1], int):
            temp += s.pop()
        if not s or s[-1] !='[':
            print(0)
            exit()
        s.pop()
        if temp == 0:
            s.append(3)
        else:
            s.append(temp * 3)
for x in s:
    if x == '(' or x == '[':
        print(0)
        exit()
print(sum(s))