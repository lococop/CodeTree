n = int(input())

# Please write your code here.

def a(n):
    return n % 2 == 0 and sum(list(map(int,str(n)))) % 5 == 0


if a(n):
    print("Yes")
else:
    print("No")