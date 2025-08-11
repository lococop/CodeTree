n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class f:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

a = [
    f(date[i], day[i], weather[i]) for i in range(n)
]

a.sort(key=lambda x:x.a)

for elem in a:
    if elem.c == 'Rain':
        print(elem.a, elem.b, elem.c)
        break