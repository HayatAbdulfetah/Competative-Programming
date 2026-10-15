amount = int(input())

bill_count = 0
bills = [100, 20, 10, 5, 1]

for bill in bills:
    bill_count += amount // bill
    amount %= bill

print(bill_count)

# Codeforces problem link --> https://codeforces.com/problemset/problem/996/A
