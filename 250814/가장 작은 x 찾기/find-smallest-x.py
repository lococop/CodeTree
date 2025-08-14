n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

MAX_NUM = 10000


def satisfy(num):

    for i in range(n):

        num *= 2

        if num < a[i] or num > b[i]:
            return False
    
    return True

for num in range(1, MAX_NUM + 1 ):

    if satisfy(num):
        print(num)
        break
    
        
        
