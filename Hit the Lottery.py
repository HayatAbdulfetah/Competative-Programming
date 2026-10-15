amount = int(input())

bill_count = 0
bills = [1, 5, 10, 20, 100]

for bill in bills:
    bill_count += amount // bill
    amount %= bill

print(bill_count)

# Codeforces problem link --> https://codeforces.com/problemset/problem/996/A
