S, Q = input().split()
S = list(S)
for i in range(int(Q)):
    a, b, c = input().split()

    if int(a) == 1:
        temp = S[int(b)-1]
        S[int(b)-1] = S[int(c)-1]
        S[int(c)-1] = temp
        print("".join(S))

    elif int(a) == 2:
        for j in range(len(S)):
            if S[j] == b:
                S[j] = c
        print("".join(S))

