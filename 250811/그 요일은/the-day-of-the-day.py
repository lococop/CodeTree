m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0,31, 29, 31, 30, 31, 30, 31,31,30,31,30,31]
a = 0
for i in range(m1):
    a += days[i]
a += d1

b = 0
for i in range(m2):
    b += days[i]
b += d2

c = (b-a)
if A == 'Mon':
    c = c
elif A == 'Tue':
    c -= 1
elif A == 'Wed':
    c -= 2
elif A == 'Thu':
    c -= 3
elif A == 'Fri':
    c -= 4
elif A == 'Sat':
    c -= 5
elif A == 'Sun':
    c -= 6

print(c//7+1)

