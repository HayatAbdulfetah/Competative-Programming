t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # At least two of the first three values are the same
    if a[0] == a[1] or a[0] == a[2]:
        common = a[0]
    else:
        common = a[1]

    for i, value in enumerate(a):
        if value != common:
            print(i + 1)
            break
          
# Codeforces problem link --> https://codeforces.com/problemset/problem/1512/A
