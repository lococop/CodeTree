n = int(input())

# Please write your code here.

def a(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += i
    
    return sum1//10

print(a(n))