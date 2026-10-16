n = int(input())
arr = list(map(int, input().split()))

evens = []
odds = []

for i, val in enumerate(arr):
    if val % 2 == 0:
        evens.append(i + 1)
    else:
        odds.append(i + 1)

if len(evens) == 1:
    print(evens[0])
else:
    print(odds[0])

# Codeforces problem link --> https://codeforces.com/problemset/problem/25/A
