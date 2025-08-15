pos = list(map(int, input().split()))

# Please write your code here.

if abs(pos[0] - pos[1]) == 1 and abs(pos[1]-pos[2]) == 1:
    print(0)

elif abs(pos[0]-pos[1]) == 2 or abs(pos[1]-pos[2]) == 2:
    print(1)
else:
    print(2)
