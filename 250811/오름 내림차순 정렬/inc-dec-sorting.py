n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
for elem in sorted(nums):
    print(elem, end = " ")

print()

for elem in sorted(nums, reverse = True):
    print(elem, end = " ")
    