a = input()

a = a.lower()

for elem in a:
    if (elem >= 'a' and elem <= 'z') or (elem >= '0' and elem <= '9'):
        print(elem, end = "")
