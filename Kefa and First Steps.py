n = int(input())
a = list(map(int, input().split()))

max_len = 1
current_len = 1

for i in range(1, len(a)):
  if a[i-1] <= a[i]:
    current_len += 1
  else:
    if current_len > max_len:
      max_len = current_len
      current_len = 1
      
if current_len > max_len:
  max_len = current_len

print(max_len)

# Codeforces problem link --> https://codeforces.com/problemset/problem/580/A
