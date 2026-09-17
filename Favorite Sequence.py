t = int(input())
for i in range(t):
    n = int(input())
    nums = input().split()
    left = 0
    right = len(nums) - 1
    result = []
  
    for j in range(n):
        if j % 2 == 0:
        	result.append(nums[left])
        	left += 1
        else:
        	result.append(nums[right])
        	right -= 1
          
    print(" ".join(result))

# codeforces problem link --> https://codeforces.com/problemset/problem/1462/A
