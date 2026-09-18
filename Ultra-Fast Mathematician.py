l1 = input()
l2 = input()

result = ""
a = [i for i in l1]
b =[i for i in l2]

for i in range(len(a)):
	if a[i] == b[i]:
		result += "0"
	else:
		result += "1"

print(result)

# codeforces problem link --> https://codeforces.com/problemset/problem/61/A
