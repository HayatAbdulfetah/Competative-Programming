n, k, l, c, d, p, nl, np = map(int, input().split())

drink = (k * l) // nl
lime = c * d
salt = p // np

toasts = min(drink, lime, salt)

print(toasts // n)

# Codeforces problem link --> https://codeforces.com/problemset/problem/151/A
