N = int(input())

arr = list(map(float, input().split()))

a = sum(arr)/len(arr)

print(f"{a:.1f}")
if a >= 4.0:
    print("Perfect")
elif a >= 3.0:
    print("Good")
else:
    print("Poor")