n = int(input())
prices = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    money = int(input())
    print(sum(price <= money for price in prices))

# Codeforces problem link --> https://codeforces.com/problemset/problem/706/B
