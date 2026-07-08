class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = power[i - 1] * 10 % MOD

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + int(s[i])

        tree = [(0, 0)] * (2 * n)

        for i, ch in enumerate(s):
            if ch != '0':
                tree[n + i] = (int(ch), 1)

        def merge(left, right):
            value = (left[0] * power[right[1]] + right[0]) % MOD
            return (value, left[1] + right[1])

        for i in range(n - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        ans = []

        for left, right in queries:
            l, r = left + n, right + n + 1
            res_left = res_right = (0, 0)

            while l < r:
                if l & 1:
                    res_left = merge(res_left, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res_right = merge(tree[r], res_right)

                l //= 2
                r //= 2

            value = merge(res_left, res_right)[0]
            digit_sum = prefix[right + 1] - prefix[left]

            ans.append(value * digit_sum % MOD)

        return ans
