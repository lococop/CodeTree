n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

class f:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

a = [
    f(name[i], korean[i], english[i], math[i]) for i in range(n)
]

a.sort(key=lambda x:(-x.b, -x.c, -x.d))

for elem in a:
    print(elem.a, elem.b, elem.c, elem.d)