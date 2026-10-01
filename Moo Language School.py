t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    ans = 0

    for i in range(0, n, k):
        group = s[i:i+k]

        if '0' not in group:
            ans += 1

    print(ans)

# Codeforces problem link --> https://codeforces.com/problemset/problem/2259/A
