N = int(input())

a = input().split()

a = "".join(a)


i = 0
j = 0
while i < len(a):

    if j < 5:
        print(a[i], end = "")
        j += 1
        
    else:
        print()
        print(a[i], end = "")
        j = 1
    i += 1
