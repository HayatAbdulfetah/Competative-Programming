t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(abs(x) for x in a)

    ops = 0
    inside = False

    for x in a:
        if x < 0:
            if not inside:
                ops += 1
                inside = True
        elif x > 0:
            inside = False
    

    print(total, ops)

# codeforces problem link --> https://codeforces.com/gym/700833/problem/E
