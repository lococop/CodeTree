a, b = map(int, input().split())

# Please write your code here.
def w(a,b):
    cnt = 0
    for i in range(a, b+1):
        if '3' in list(str(i)) or '6' in list(str(i)) or '9' in list(str(i)) or i % 3 == 0:
            cnt += 1
    return cnt

print(w(a,b))
