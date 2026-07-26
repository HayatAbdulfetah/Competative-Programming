n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total = sum(coins)
my_sum = 0
count = 0

for coin in coins:
    my_sum += coin
    count += 1

    if my_sum > total - my_sum:
        break

print(count)

# problem link --> https://codeforces.com/problemset/problem/160/A
