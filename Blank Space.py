t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    count = 0

    for x in a:
        if x == 0:
            count += 1
            ans = max(ans, count)
        else:
            count = 0

    print(ans)

# problem link --> https://codeforces.com/problemset/problem/1829/B
