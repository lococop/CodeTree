secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class f:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


f1 = f(secret_code, meeting_point, time)

print("secret code :", f1.a)
print("meeting point :", f1.b)
print("time :", f1.c)