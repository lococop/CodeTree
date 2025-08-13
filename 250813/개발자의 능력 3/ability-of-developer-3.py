abilities = list(map(int, input().split()))

# Please write your code here.

import sys
min_diff = sys.maxsize

def get_diff(i, j, k):
    sum1 = abilities[i] + abilities[j] + abilities[k]
    sum2 = sum(abilities) - sum1

    return abs(sum1-sum2)

for i in range(len(abilities)):
    for j in range(i+1, len(abilities)):
        for k in range(j+1, len(abilities)):

            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)