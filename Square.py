t = int(input())

for _ in range(t):
    points = []

    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))

    xs = [p[0] for p in points]

    side = max(xs) - min(xs)

    print(side * side)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1921/A
