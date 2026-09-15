t = int(input())
for _ in range(t):
  expression = input()
  
  s = expression.split("+")
  ans = [int(i) for i in s]
  
  print(sum(ans))

# Codeforces problem link --> https://codeforces.com/problemset/problem/1772/A
