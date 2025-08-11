n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class f:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


a = [
    f(name[i], score1[i], score2[i], score3[i]) for i in range(n)
]

a.sort(key=lambda x:(x.b+x.c+x.d))

for elem in a:
    print(elem.a, elem.b, elem.c, elem.d)