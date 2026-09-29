from collections import Counter

q = int(input())
for _ in range(q):
  n = int(input())
  s, t = map(str, input().split())

  ss = Counter(s)
  tt = Counter(t)

  if ss == tt:
    print("YES")
  else:
    print("NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/2167/B
