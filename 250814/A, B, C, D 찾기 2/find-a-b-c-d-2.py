nums = list(map(int, input().split()))

# Please write your code here.

MaxN = 41

for a in range(1, MaxN):
    for b in range(a, MaxN):
        for c in range(b, MaxN):
            for d in range(c, MaxN):

                arr = [a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]

                if sorted(arr) == sorted(nums):
                    print(a, b, c, d)
                    break