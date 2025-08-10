a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def plus(a,c):
    return a+c
def minus(a,c):
    return a-c
def odd(a,c):
    return a*c
def division(a,c):
    return a/c


if o == '+':
    print(f"{a} + {c} = {plus(a,c)}")
elif o == '-':
    print(f"{a} - {c} = {minus(a,c)}")
elif o == '*':
    print(f"{a} * {c} = {odd(a,c)}")
elif o == '/':
    print(f"{a} / {c} = {division(a,c)}")
else:
    print("False")