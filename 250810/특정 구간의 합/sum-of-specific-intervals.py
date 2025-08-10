n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def w(n,m,arr,queries):

    for a in queries:
        sum1 = 0
        for i in range(a[0]-1, a[1]):
            sum1 += arr[i]
        print(sum1)

w(n,m,arr,queries)