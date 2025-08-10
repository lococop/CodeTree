A = input()
B = input()

# Please write your code here.
while True:
    if B in A:
        a = A.index(B)
        A = list(A)
        for i in range(len(B)):
            A.pop(a)
        A = "".join(A)
    else:
        break

print(A) 
