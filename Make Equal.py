t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    avg = sum(arr) // n
    extra = 0
    possible = True

    for i in range(n - 1):
        water = arr[i] + extra

        if water < avg:
            possible = False
            break

        extra = water - avg

    if possible:
        print("YES")
    else:
        print("NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/1931/B
