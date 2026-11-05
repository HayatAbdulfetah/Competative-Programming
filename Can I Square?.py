import math

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  total = sum(a)
  root = int(total ** 0.5)

  if total == root ** 2:
    print("YES")
  else:
    print("NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/1915/C
