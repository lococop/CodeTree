a, b, c = map(int, input().split())

Is = False
for i in range(a, b+1):
    if i % c == 0:
        Is = True

if Is:
    print("NO")
else:
    print("YES")