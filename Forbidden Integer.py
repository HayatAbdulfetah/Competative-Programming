t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    if x != 1:
        ans = [1] * n

    elif k == 1 or (k == 2 and n % 2 != 0):
        ans = []

    elif n % 2 == 0:
        ans = [2] * (n // 2)

    else:
        ans = [3] + [2] * ((n - 3) // 2)

    if ans:
        print("YES")
        print(len(ans))
        print(*ans)
    else:
        print("NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/1845/A
