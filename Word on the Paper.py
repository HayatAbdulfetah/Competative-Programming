t = int(input())
for _ in range(t):
  word = ""
  for i in range(8):
    grid = input()
    
    for j in range(8):
      if grid[j].isalpha():
        word += grid[j]
        
  print(word)
  
# Codeforces problem link --> https://codeforces.com/problemset/problem/1850/C
