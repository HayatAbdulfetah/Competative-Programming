import math

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  x = min(a) + 1
  a[a.index(min(a))] = x

  ans = math.prod(a)

  print(ans)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1873/B
