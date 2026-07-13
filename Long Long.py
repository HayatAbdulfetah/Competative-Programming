t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    summ = 0
    total_count = 0
    negative_count = 0
    
    for x in a:
        summ += abs(x)

        if x > 0:
            total_count += negative_count
            negative_count = 0
            
        elif x < 0:
            negative_count = 1
    
    total_count += negative_count
    
    print(summ, total_count)

# codeforces problem link --> https://codeforces.com/gym/700833/problem/E
