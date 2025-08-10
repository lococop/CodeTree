text = input()
pattern = input()

# Please write your code here.

def w(a,b):
    if b in a:
        return a.index(b)
    else:
        return -1
    

print(w(text, pattern))