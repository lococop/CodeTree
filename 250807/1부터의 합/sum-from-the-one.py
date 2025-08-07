N = int(input())

sum = 0
for i in range(1, 101):
    
    if sum+i >= N:
        print(sum)
        break
    sum += i
