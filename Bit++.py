n = int(input())
x = 0
for i in range(n):
	st = input()
	if '++' in st:
		x += 1
	else:
		x -= 1
print(x)

# problemlink --> https://codeforces.com/problemset/problem/282/A
