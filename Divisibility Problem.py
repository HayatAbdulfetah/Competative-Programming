t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  rem = a % b
  if rem == 0:
    print(0)
  else:
    ans = b - rem
    print(ans)

# codeforces proplem link --> https://codeforces.com/problemset/problem/1328/A
