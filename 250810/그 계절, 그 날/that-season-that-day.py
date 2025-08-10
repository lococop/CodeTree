Y, M, D = map(int, input().split())

# Please write your code here.

def w(Y,M,D):
    Is_Yoon = False

    if Y % 4 == 0:
        if Y % 100 == 0 and Y % 400 != 0:
            Is_Yoon = False
        else:
            Is_Yoon = True

    if Is_Yoon:
        if M in [1,3,5,7,8,10,12]:
            if D >= 1 and D <= 31:
                pass
            else:
                return -1
        elif M in [4,6,9,11]:
            if D >= 1 and D <= 30:
                pass
            else:
                return -1
        elif M == 2:
            if D >= 1 and D <= 29:
                pass
            else:
                return -1

        if M >= 3 and M <= 5:
            return "Spring"
        elif M >= 6 and M <= 8:
            return "Summer"
        elif M >= 9 and M <= 11:
            return "Fall"
        elif M in [12,1,2]:
            return "Winter"

    else:
        if M in [1,3,5,7,8,10,12]:
            if D >= 1 and D <= 31:
                pass
            else:
                return -1
        elif M in [4,6,9,11]:
            if D >= 1 and D <= 30:
                pass
            else:
                return -1
        elif M == 2:
            if D >= 1 and D <= 28:
                pass
            else:
                return -1

        if M >= 3 and M <= 5:
            return "Spring"
        elif M >= 6 and M <= 8:
            return "Summer"
        elif M >= 9 and M <= 11:
            return "Fall"
        elif M in [12,1,2]:
            return "Winter"
        
print(w(Y,M,D))