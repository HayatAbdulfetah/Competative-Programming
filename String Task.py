word = input().lower()
vowels = ["a","o","y","e","u","i"]
letter = ""
a =[i for i in word]
for i in range(len(a)):
	if a[i] in vowels:
		continue
	else:
		letter += "."
		letter += a[i]
print(letter)

# problem link --> https://codeforces.com/problemset/problem/118/A
