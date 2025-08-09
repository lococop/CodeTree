N = int(input())

cnt = 1
cnt5 = 0
while True:
    a = N*cnt 
    print(a, end = " ")
    cnt += 1
    if a % 5 == 0:
        cnt5 += 1
    
    if cnt5 == 2:
        break