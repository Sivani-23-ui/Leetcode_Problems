class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i + 1] = dp[i]

            for j in range(i, -1, -1):
                if s[j] == s[i]:
                    if i - j <= 1 or pal[j + 1][i - 1]:
                        pal[j][i] = True

                        if i - j + 1 >= k:
                            dp[i + 1] = max(dp[i + 1], dp[j] + 1)
        return dp[n]