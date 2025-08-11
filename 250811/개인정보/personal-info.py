n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class f:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

a = [
    f(name[i], height[i], weight[i]) for i in range(5)
]

a.sort(key=lambda x:x.a)
print("name")
for elem in a:
    print(elem.a, elem.b, elem.c)
print()
a.sort(key=lambda x:-x.b)
print("height")
for elem in a:
    print(elem.a, elem.b, elem.c)