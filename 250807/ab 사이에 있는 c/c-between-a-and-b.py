a, b, c = map(int, input().split())

IsC = False
for i in range(a, b+1):
    if i % c == 0:
        IsC = True

if IsC == True:
    print("YES")
else:
    print("NO")