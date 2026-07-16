s = input()

target = "hello"
i = 0

for c in s:
    if c == target[i]:
        i += 1
        if i == 5:
            break

if i == 5:
    print("YES")
else:
    print("NO")


# problem link --> https://codeforces.com/problemset/problem/58/A
