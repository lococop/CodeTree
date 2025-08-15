n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.




for i in range(n):
    max_x1 = 0
    min_x2 = 101
    for j in range(n):
        if i == j:
            continue
        else:
            max_x1 = max(max_x1, x1[j])
            min_x2 = min(min_x2, x2[j])


    if max_x1 <= min_x2:
        print("Yes")
        break

    if i == n-1:
        print("No")
    