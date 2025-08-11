n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def gcd(a, b):
    # 최대공약수 (유클리드 호제법, 재귀)
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(arr, n):
    # n개의 숫자의 LCM을 재귀로 구함
    if n == 1:
        return arr[0]
    return lcm(arr[n-1], lcm_list(arr, n-1))


print(lcm_list(arr, n))