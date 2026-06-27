from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = Counter()
    ans = 0

    for x in a:
        if cnt[k - x] > 0:
            ans += 1
            cnt[k - x] -= 1
        else:
            cnt[x] += 1

    print(ans)

# codeforces problem link --> https://codeforces.com/gym/700833/problem/D
