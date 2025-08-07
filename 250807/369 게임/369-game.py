N = int(input())

for i in range(1, N+1):
    if i % 3 == 0:
        print(0, end = " ")
    else:
        a = False
        for j in str(i):
            if j in ['3', '6', '9']:
                print(0, end = " ")
                a = True

        if a == False:
            print(i, end = " ")
            
    