class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True 
        max_reach = 0
        
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        return False

      
# problem link --> https://leetcode.com/problems/jump-game/
