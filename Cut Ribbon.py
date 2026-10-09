n, a, b, c = map(int, input().split())

dp = [-1] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for length in (a, b, c):
        if i >= length and dp[i - length] != -1:
            dp[i] = max(dp[i], dp[i - length] + 1)

print(dp[n])

# Codeforces problem link --> https://codeforces.com/problemset/problem/189/A
