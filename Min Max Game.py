t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = sum(a)
    zeros = n - ones

    if ones >= zeros:
        print("Bessie")
    else:
        print("Elsie")

# Codeforces problem link --> https://codeforces.com/problemset/problem/2263/A
