n = int(input())

# Please write your code here.
def square(n):
    cnt = 0
    for _ in range(n):
        for _ in range(n):
            cnt += 1
            print(cnt, end = " ")
            if cnt == 9:
                cnt = 0
        print()

square(n)