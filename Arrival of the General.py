n = int(input())
a = list(map(int, input().split()))

tallest = a.index(max(a))
shortest = n - 1 - a[::-1].index(min(a))

swaps = tallest + (n - 1 - shortest)

if tallest > shortest:
    swaps -= 1

print(swaps)

# Codeforces problem link --> https://codeforces.com/problemset/problem/144/A
