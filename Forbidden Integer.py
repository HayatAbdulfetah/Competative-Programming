
t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    if x != 1:
        print("YES")
        print(n)
        print(*([1] * n))

    elif k == 1:
        print("NO")

    elif k == 2:
        if n % 2 == 0:
            print("YES")
            print(n // 2)
            print(*([2] * (n // 2)))
        else:
            print("NO")

    else:
        if n % 2 == 0:
            print("YES")
            print(n // 2)
            print(*([2] * (n // 2)))
        else:
            print("YES")
            print((n - 3) // 2 + 1)
            print(3, *([2] * ((n - 3) // 2)))

# Codeforces problem link --> https://codeforces.com/problemset/problem/1845/A
