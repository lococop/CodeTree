word1 = input()
word2 = input()

# Please write your code here.
if list(word1.lower()).sort() == list(word2.lower()).sort() and len(word1) == len(word2):
    print("Yes")
else:
    print("No")