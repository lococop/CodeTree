a, b = map(int, input().split())
n = input()

# Please write your code here.

m = 0
for i in range(len(n)):
    m = m*a + int(n[i])

arr = []
while True:
    if m < b:
        arr.append(m)
        break
    
    arr.append(m%b)
    m //= b

for elem in arr[::-1]:
    print(elem, end = "")