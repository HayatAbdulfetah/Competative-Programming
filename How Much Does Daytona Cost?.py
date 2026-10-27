t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if k in arr:
        print("YES")
    else:
        print("NO")


# Codeforces problem link --> https://codeforces.com/problemset/problem/1878/A
