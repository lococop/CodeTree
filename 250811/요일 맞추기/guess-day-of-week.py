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

c = (b-a)%7
if c == 0:
    print("Mon")
elif c == 1:
    print("Tue")
elif c == 2:
    print("Wed")
elif c == 3:
    print("Thu")
elif c == 4:
    print("Fri")
elif c == 5:
    print("Sat")
elif c == 6:
    print("Sun")
