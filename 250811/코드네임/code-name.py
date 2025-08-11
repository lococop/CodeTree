MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class f:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score
a = [
    f(codenames[0], scores[0]),
    f(codenames[1], scores[1]),
    f(codenames[2], scores[2]),
    f(codenames[3], scores[3]),
    f(codenames[4], scores[4]),
]

import sys
min_n = sys.maxsize
min_class = None

for i in range(MAX_N):
    if min_n > a[i].score:
        min_n = a[i].score
        min_class = a[i]


print(min_class.codename, min_class.score)

