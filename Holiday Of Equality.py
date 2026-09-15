n = int(input())
S = 0
a = [int(i) for i in input().split()]
x = max(a)

for i in range(n):
	y = x - a[i]
	S += y
	
print(S)

# Codeforces problem link --> https://codeforces.com/problemset/problem/758/A
