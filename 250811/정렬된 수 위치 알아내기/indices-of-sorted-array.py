n = int(input())
sequence = list(map(int, input().split()))

a = sorted(sequence)
used = [False] * n  # 인덱스 사용 여부
arr = []

for i in range(n):
    for j in range(n):
        if sequence[i] == a[j] and not used[j]:
            arr.append(j+1)  # 1-based index
            used[j] = True   # 사용 처리
            break

print(*arr)
