t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    print("First" if a + c > b else "Second")

# Codeforces problem link --> https://codeforces.com/problemset/problem/1858/A
