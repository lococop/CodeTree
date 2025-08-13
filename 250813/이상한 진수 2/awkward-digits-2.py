a = input()

# Please write your code here.

Max_Num = ""

for i in range(len(a)):
    if a[i] == '0':
        Max_Num += '1'
        Max_Num += a[i+1:]
        break
    elif i == len(a)-1:
        Max_Num += '0'
        break
    else:
        Max_Num += a[i]

    

ans = 0

for i in range(len(Max_Num)):
    ans = ans * 2 + int(Max_Num[i])

print(ans)
    