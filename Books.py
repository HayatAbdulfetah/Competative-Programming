n, t = map(int, input().split())
books = list(map(int, input().split()))

left = total = answer = 0

for right in range(n):
    total += books[right]

    while total > t:
        total -= books[left]
        left += 1

    answer = max(answer, right - left + 1)

print(answer)

# Codeforces problem link --> https://codeforces.com/problemset/problem/279/B
