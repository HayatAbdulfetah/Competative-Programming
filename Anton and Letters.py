s = input()

letters = set()

for ch in s:
    if ch.isalpha():
        letters.add(ch)

print(len(letters))

# problem link  --> https://codeforces.com/problemset/problem/443/A
