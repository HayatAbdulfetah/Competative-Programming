n = int(input())
for i in range(n):
    word = input()
    l = len(word)
    if l > 10:
        print(word[0] + str(len(word)-2) + word[l-1])
    else:
        print(word)

# problem link --> https://codeforces.com/problemset/problem/71/A
