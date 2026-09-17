t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    count = 0
  
    for i in range(n):
        a = list(s)
        if a[i] == '0':
            a[i] = '1'
        else:
            a[i] = '0'
          
        for char in a:
            if char == '1':
                count += 1
              
    print(count)

# Codeforces problem link --> https://codeforces.com/problemset/problem/2106/A
