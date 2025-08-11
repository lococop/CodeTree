product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class f:
    def __init__(self, a,b):
        self.a = a
        self.b = b

f1 = f(product_name, product_code)
f2 = f(product_name, product_code)

f2.a = "codetree"
f2.b = 50

print("product", f2.b, "is", f2.a)
print("product", f1.b, "is", f1.a)
