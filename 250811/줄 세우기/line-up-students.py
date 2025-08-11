n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class f:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

students.sort(key=lambda x:(-x[0], -x[1], x[2]))

for elem in students:
    print(elem[0], elem[1], elem[2])