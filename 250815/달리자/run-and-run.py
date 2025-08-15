n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

move_cnt = 0

d = 0
for i in range(n-1):

    move_cnt = A[i]+move_cnt - B[i]

    d += move_cnt

print(d)