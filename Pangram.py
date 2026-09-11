n = int(input())
s = input()
alphabetSet = set("abcdefghijklmnopqrstuvwxyz")
inputSet = set(s.lower())
if alphabetSet.issubset(inputSet):
    print("YES")
else:
    print ("NO")

# Codeforces problem link --> https://codeforces.com/problemset/problem/520/A
