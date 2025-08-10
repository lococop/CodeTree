n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def w(n1, n2, a, b):
    Is = False
    cnt = 0
    s = 0
    for i in range(n1):
        if cnt == 3:
            Is = True
            break
        for j in range(s, n2):
            if a[i] == b[j]:
                
                cnt += 1
                s = j+1
                break
            else:
                break

    return Is

if w(n1,n2,a,b):
    print("Yes")
else:
    print("No")