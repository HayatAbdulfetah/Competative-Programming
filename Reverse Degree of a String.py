class Solution:
    def reverseDegree(self, s: str) -> int:
        chars = 'zyxwvutsrqponmlkjihgfedcba'
        ans = 0
        for i in range(len(s)):
            ans += (i + 1) * (chars.index(s[i]) + 1)

        return ans
