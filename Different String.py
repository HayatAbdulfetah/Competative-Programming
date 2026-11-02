t = int(input())

for _ in range(t):
    s = input()

    if len(set(s)) == 1:
        print("NO")
    else:
        s = list(s)

        for i in range(1, len(s)):
            if s[i] != s[0]:
                s[0], s[i] = s[i], s[0]
                break

        print("YES")
        print("".join(s))

# Codeforces problem link --> https://codeforces.com/problemset/problem/1971/B
