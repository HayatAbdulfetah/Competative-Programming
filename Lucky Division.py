n = int(input())

def lucky(x):
    while x > 0:
        d = x % 10
        if d != 4 and d != 7:
            return False
        x //= 10
    return True

for i in range(1, n + 1):
    if lucky(i) and n % i == 0:
        print("YES")
        break
else:
    print("NO")

# problem link --> https://codeforces.com/problemset/problem/122/A
