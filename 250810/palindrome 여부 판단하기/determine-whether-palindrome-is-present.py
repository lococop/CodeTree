A = input()

# Please write your code here.

def w(A):
    temp = ''
    for i in range(len(A)-1, -1, -1):
        temp += A[i]
    
    if A == temp:
        print("Yes")
    else:
        print("No")

w(A)
        