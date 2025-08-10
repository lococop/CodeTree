a = input()
b = int(input())

for i in range(len(a)-1, len(a)-b-1, -1):
    print(a[i], end = "")