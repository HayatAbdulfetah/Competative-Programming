amount = int(input())

bill_count = 0

for bill in [100, 20, 10, 5, 1]:
    bill_count += amount // bill
    amount %= bill

print(bill_count)

# Codeforces proble link --> https://codeforces.com/problemset/problem/996/A
