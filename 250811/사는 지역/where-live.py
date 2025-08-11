n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class f:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


a = [
    f(name[i], street_address[i], region[i]) for i in range(n)
]

a.sort(key=lambda x: x.a)

print("name", a[-1].a)
print("addr", a[-1].b)
print("city", a[-1].c)