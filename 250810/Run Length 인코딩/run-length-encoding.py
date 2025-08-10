A = input()

# Please write your code here.
a = A[0]
cnt = 0
result = A[0]

for elem in A:
    if a != elem:
        a = elem
        result += str(cnt)
        result += elem
        cnt = 1
    else:
        cnt += 1

result += str(cnt)
        
print(len(result))
print(result)