a = [input() for _ in range(10)]
b = input()

Is = False
for elem in a:
    if elem[-1] == b:
        print(elem)
        Is = True

if Is == False:
    print("None")
