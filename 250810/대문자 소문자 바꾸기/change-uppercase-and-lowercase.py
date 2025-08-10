a = input()

for elem in a:
    if elem >= 'A' and elem <= 'Z':
        print(elem.lower(),end="")
    elif elem >= 'a' and elem <= 'z':
        print(elem.upper(),end="")