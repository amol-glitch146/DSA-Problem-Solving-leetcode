class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] means: does s[:i] match p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* ...
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # Case 1: Treat "x*" as empty
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: Use '*' to match one or more of preceding element
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]
        
        return dp[m][n]
