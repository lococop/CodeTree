M, D = map(int, input().split())

# Please write your code here.

def w(M, D):
    if M in [1,3,5,7,8,10,12]:
        if D >= 1 and D <= 31:
            return "Yes"
    elif M in [4,6,9,11]:
        if D >= 1 and D <= 30:
            return "Yes"
    elif M == 2:
        if D >= 1 and D <= 28:
            return "Yes"
    
    return "No"

print(w(M,D))