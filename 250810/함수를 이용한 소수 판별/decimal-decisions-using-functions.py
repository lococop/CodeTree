a, b = map(int, input().split())

# Please write your code here.

def w(a,b):
    sum1 = 0
    

    for i in range(a, b+1):
        IsPrime = True
        for j in range(2, i):
            if i % j == 0:
                IsPrime = False
        
        if IsPrime == True:
            sum1 += i

    return sum1

print(w(a,b))
        
            