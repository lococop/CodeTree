n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

students.sort(key=lambda x:(x[0], -x[1]))

for elem in students:
    print(elem[0], elem[1], elem[2])