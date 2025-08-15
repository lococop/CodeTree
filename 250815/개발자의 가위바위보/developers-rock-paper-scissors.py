N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.

max_win = 0


win = 0
for i in range(N):
    if a[i] == 1 and b[i] == 2:
        win += 1
    elif a[i] == 2 and b[i] == 3:
        win += 1
    elif a[i] == 3 and b[i] == 1:
        win += 1
    
max_win = max(max_win, win)

win = 0
for i in range(N):
    if a[i] == 1 and b[i] == 3:
        win += 1
    elif a[i] == 3 and b[i] == 2:
        win += 1
    elif a[i] == 2 and b[i] == 1:
        win += 1
    
max_win = max(max_win, win)

print(max_win)