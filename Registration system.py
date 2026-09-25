n = int(input())

users = {}

for _ in range(n):
    s = input()

    if s not in users:
        users[s] = 0
        print("OK")
    else:
        users[s] += 1
        print(s + str(users[s]))


# Codeforrces problem link --> https://codeforces.com/problemset/problem/4/C
