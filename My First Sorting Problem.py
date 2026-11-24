t = int(input())
for _ in range(t):
  x, y = map(int, input().split())
  if x > y:
    print(y, x)
  else:
    print(x, y)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1971/A
