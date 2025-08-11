unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class f:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c


f1 = f(unlock_code, wire_color, seconds)

print("code :", f1.a)
print("color :", f1.b)
print("second :", f1.c)