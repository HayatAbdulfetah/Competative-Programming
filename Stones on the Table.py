n = int(input())
s = input()
stones = 0

for i in range(1, len(s)):
 if s[i]==s[i-1]:
  stones += 1
  
print(stones)

# Codeforces problem link --> https://codeforces.com/problemset/problem/266/A
