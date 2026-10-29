import sys

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]

    max_len = 1
    current_len = 1

    for i in range(1, n):
        if a[i] >= a[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1

    if current_len > max_len:
        max_len = current_len

    print(max_len)

# Codeforces problem link --> https://codeforces.com/problemset/problem/580/A
