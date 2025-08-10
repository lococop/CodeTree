a = input()
a = list(a)

while len(a) != 1:
    b = int(input())
    if b > len(a)-1:
        a.pop(-1)
    else:
        a.pop(b)
    print("".join(a))