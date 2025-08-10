A = input()

# Please write your code here.

def w(A):
    a = A[0]
    cnt = 0
    for i in range(1, len(A)):
        if a != A[i]:
            cnt += 1
    if cnt >= 2:
        print("Yes")
    else:
        print("No")

w(A)