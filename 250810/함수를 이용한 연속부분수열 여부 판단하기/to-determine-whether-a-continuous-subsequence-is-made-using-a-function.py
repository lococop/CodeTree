n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def w(n1, n2, a, b):
    sum1 = ''
    sum2 = ''

    for elem in a:
        sum1 += str(elem)
    for elem in b:
        sum2 += str(elem)
    Is = False
    if sum2 in sum1:
        Is = True
    

    return Is

if w(n1,n2,a,b):
    print("Yes")
else:
    print("No")