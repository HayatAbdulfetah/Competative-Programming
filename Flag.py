n, m = map(int, input().split())

flag = [input() for _ in range(n)]

for i in range(n):
    if len(set(flag[i])) != 1:
        print("NO")
        break

    if i > 0 and flag[i] == flag[i-1]:
        print("NO")
        break
else:
    print("YES")


# Codeforces problem link --> https://codeforces.com/problemset/problem/16/A
