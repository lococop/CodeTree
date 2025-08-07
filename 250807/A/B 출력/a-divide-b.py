A, B = map(int, input().split())

a = str(A//B)
b = A%B
temp = ""
for i in range(20):
    temp += str(b*10//B)
    b = b*10%B

print(a+"."+temp)

