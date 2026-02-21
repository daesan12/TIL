str = input()
result ="Yes"
s= []
for i in str:
    if i =='(':
        s.append(i)
    else:
        if len(s) == 0:
            result = "No"
            break
        s.pop()
    if s:
        result = "No"

print(result)
