a = ['apple', 'banana', 'grape', 'blueberry', 'orange']

b = input()

arr = []
cnt = 0

for elem in a:
    if elem[2] == b or elem[3] == b:
        arr.append(elem)
        cnt += 1

for elem in arr:
    for i in elem:
        print(i, end = "")
    print()

print(cnt)