class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        digits = sorted(n)

        ans = int(digits[-1]) * int(digits[-2])

        return ans

# LeetCode problem link --> https://leetcode.com/problems/maximum-product-of-two-digits/description/?envType=daily-question&envId=2026-07-25
