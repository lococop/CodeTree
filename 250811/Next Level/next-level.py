user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class f:
    def __init__(self, a,b):
        self.a = a
        self.b = b


f1 = f(user2_id, user2_level)
f2 = f(user2_id, user2_level)

f2.a = "codetree"
f2.b = 10

print("user", f2.a, "lv", f2.b)
print("user", f1.a, "lv", f1.b)


