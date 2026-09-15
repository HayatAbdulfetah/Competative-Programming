t = int(input())
for i in range(t):
	x = [(i) for i in input().split()]
	str = ""
	for j in x:
		str += j[0]
	print(str)
