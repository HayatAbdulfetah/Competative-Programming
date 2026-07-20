n = int(input())
integers = [int(n) for n in input().split()]
police = 0
crime = 0

for n in integers:
    if n == -1:
        if police > 0:
            police -= 1
        else:
            crime += 1
    else:
        police += n
        
print(crime)

# problem link --> https://codeforces.com/problemset/problem/427/A
