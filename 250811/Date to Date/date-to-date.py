m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31, 28, 31, 30, 31, 30, 31,31,30,31,30,31]

a = 0
for i in range(m1):
    a += days[i]
a += d1

b = 0
for i in range(m2):
    b += days[i]

b += d2

print(b-a+1)