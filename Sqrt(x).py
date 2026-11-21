class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(sqrt(x))
        left = 1
        right = x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq > x:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid

        return ans
