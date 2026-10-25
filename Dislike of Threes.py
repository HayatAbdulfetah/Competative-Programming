t = int(input())

for _ in range(t):
    k = int(input())

    num = 0
    count = 0

    while count < k:
        num += 1

        if num % 3 != 0 and num % 10 != 3:
            count += 1

    print(num)
  
# codeforces problem link --> https://codeforces.com/problemset/problem/1560/A
