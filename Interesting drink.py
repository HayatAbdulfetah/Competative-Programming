import sys
from bisect import bisect_right

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
prices = sorted(data[1:n + 1])
q = data[n + 1]
budgets = data[n + 2:n + 2 + q]

print("\n".join(str(bisect_right(prices, budget)) for budget in budgets))

# Codeforces problem link --> https://codeforces.com/problemset/problem/706/B
