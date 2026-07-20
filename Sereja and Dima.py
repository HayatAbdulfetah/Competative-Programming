n = int(input())
cards = list(map(int, input().split()))

left, right = 0, n - 1
S, D = 0, 0

for i in range(n):
    if cards[left] > cards[right]:
        picked = cards[left]
        left += 1
    else:
        picked = cards[right]
        right -= 1
    
    if i % 2 == 0:
        S += picked
    else:
        D += picked

print(S, D)

# problem link --> https://codeforces.com/problemset/problem/381/A
