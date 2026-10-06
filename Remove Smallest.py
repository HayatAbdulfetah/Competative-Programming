t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    possible = all(a[i] - a[i - 1] <= 1 for i in range(1, n))
    print("YES" if possible else "NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/1399/A
