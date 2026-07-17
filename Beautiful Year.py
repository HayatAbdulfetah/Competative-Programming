year = int(input())

while True:
    year += 1
    
    if len(set(str(year))) == 4:
        print(year)
        break

# problem link --> https://codeforces.com/problemset/problem/271/A
