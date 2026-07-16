c = int(input())
count = 0
pre=""

for i in range(c):
	a = input()
	if (a != pre):
		count+=1 
		
	pre = a
	
print(count)

# problem link --> https://codeforces.com/problemset/problem/344/A
