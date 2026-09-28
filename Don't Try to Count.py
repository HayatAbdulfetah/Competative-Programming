t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  x = input()
  s = input()

  ans = 0
  
  while s not in x and len(x) <= 25:
    x += x
    ans += 1

  if s in x:
    print(ans)
  else:
    print(-1)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1881/A
