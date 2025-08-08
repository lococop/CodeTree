N = int(input())

for i in range(11,N*2+11,2):
    for j in range(0,N*2,2):
        print(i+j, end = " ")
    print()