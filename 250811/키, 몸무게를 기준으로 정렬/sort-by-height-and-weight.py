n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class f:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

a = [
    f(name[i], height[i], weight[i]) for i in range(n)
]

a.sort(key=lambda x:(x.b, -x.c))

for elem in a:
    print(elem.a, elem.b, elem.c)