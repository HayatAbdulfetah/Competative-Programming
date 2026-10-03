a = [int(i) for i in input().split()]
s = input()
cal = 0

for i in s:
    cal += a[int(i)-1]
    
#we can use cal = sum(a[int(x)-1] for x in s) istead of using the for loop

print(cal)

# Codeforces problem link -->
