n, h = map(int, input().split())
friends = [int(i) for i in input().split()]

width  = 0

for f in friends:
    
    if f > h:
        
        #handle the case when the height of the person exceeds the hieght of the fence
        width += 1
    
    width += 1
    
print(width)

# Codeforces problem link --> https://codeforces.com/problemset/problem/677/A
