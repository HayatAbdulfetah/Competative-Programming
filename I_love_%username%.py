n = int(input())
a = list(map(int, input().split()))

maximum = a[0]
minimum = a[0]
count = 0

for i in range(1, n):

    if a[i] > maximum:
        count += 1
        maximum = a[i]

    elif a[i] < minimum:
        count += 1
        minimum = a[i]

print(count)

# Codeforces problem link --> https://codeforces.com/problemset/problem/155/A
