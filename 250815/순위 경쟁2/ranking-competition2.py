n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
score = [0]*2

mungye = ["A", "B"]

cnt = 0

for i in range(n):
    if c[i] == 'A':
        score[0] += s[i]
    elif c[i] == 'B':
        score[1] += s[i]

    if score[0] == score[1]:
        temp = mungye
        mungye = ["A", "B"]

    
    elif score[0] > score[1]:
        temp = mungye
        mungye = ["A"]

    elif score[0] < score[1]:
        temp = mungye
        mungye = ["B"]

    if temp != mungye:
        cnt += 1

print(cnt)