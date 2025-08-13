n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

arr_size = 101
arr = ['0'] * arr_size

for i in range(n):
    arr[pos[i]] = alpha[i]

max_size = 0

for i in range(arr_size):
    for j in range(i + 1, arr_size):
        
        if arr[i] == '0' and arr[j] == '0':
            continue

        cntG = 0
        cntH = 0
        
        for k in range(i, j + 1):
            if arr[k] == 'G':
                cntG += 1
            elif arr[k] == 'H':
                cntH += 1
        
        if (cntG == cntH and cntG > 0) or (cntG > 0 and cntH == 0) or (cntH > 0 and cntG == 0):
            first_person = -1
            last_person = -1
            
            for k in range(i, j + 1):
                if arr[k] != '0':
                    if first_person == -1:
                        first_person = k
                    last_person = k
            
            if first_person != -1:
                current_size = last_person - first_person
                max_size = max(max_size, current_size)

print(max_size)