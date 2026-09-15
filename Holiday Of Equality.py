n = int(input())
S = 0
a = [int(i) for i in input().split()]
for i in range(n):
	x = max(a)
	y = x - a[i]
	S += y
print(S)

# Codeforces problem link --> https://codeforces.com/problemset/problem/758/A
