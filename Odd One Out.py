t = int(input())
for i in range(t):
	a,b,c = map(int,input().split())
	if a == b and c != a:
		print(c)
	elif a == c and b !=a:
		print(b)
	elif b == c and a != b:
		print(a)
	else:
		print(a)

    
# Codeforces problem link --> https://codeforces.com/problemset/problem/1915/A
