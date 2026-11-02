t = int(input())

for _ in range(t):
  s = input()
  if len(set(s)) == 1:
    print("NO")
  else:
    print("YES")
    print(s[::-1])

# Codeforces problem link --> https://codeforces.com/problemset/problem/1971/B
