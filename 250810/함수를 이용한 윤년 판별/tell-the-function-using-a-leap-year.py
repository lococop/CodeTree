y = int(input())

# Please write your code here.

def w(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        return True

if w(y):
    print("true")
else:
    print("false")