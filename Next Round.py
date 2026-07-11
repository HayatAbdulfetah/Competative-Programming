n, k = map(int, input().split())
scores = list(map(int, input().split()))
threshold = scores[k - 1]
qualified = sum(1 for score in scores if score >= threshold and score > 0)

print(qualified)


# problem link --> https://codeforces.com/problemset/problem/158/A
