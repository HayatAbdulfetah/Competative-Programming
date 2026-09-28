t = int(input())

for _ in range(t):
    s = input()

    if s == "abc":
        print("YES")
    elif s == "acb":
        print("YES")
    elif s == "bac":
        print("YES")
    elif s == "cba":
        print("YES")
    else:
        print("NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/1873/A
