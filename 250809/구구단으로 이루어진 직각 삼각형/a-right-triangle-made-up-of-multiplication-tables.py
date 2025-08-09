N = int(input())

for i in range(1, N+1):
    for j in range(1, N+2-i):
        if j == N+1-i:
            print(f"{i} * {j} = {i*j}")
        else:    
            print(f"{i} * {j} = {i*j} /", end = " ")