word = input()

if len(word) == 1 or word.isupper() or word[1:].isupper():
    word = word.swapcase()

print(word)

# Codeforces problem link --> https://codeforces.com/problemset/problem/131/A
