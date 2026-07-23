s = input()

count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        count = 1

    if count >= 7:
        print("YES")
        break
else:
    print("NO")

# problem link --> https://codeforces.com/problemset/problem/96/A
