a, b = map(int, input().split())

# Please write your code here.

def w(a,b):
    cnt = 0 
    for i in range(a, b+1):
        IsPrime = True
        for j in range(2, i):
            if i % j == 0:
                IsPrime = False
        if IsPrime == True and sum(list(map(int,str(i)))) % 2 == 0:
            cnt += 1

    return cnt

print(w(a,b))