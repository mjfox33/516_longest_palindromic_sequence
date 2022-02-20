from collections import defaultdict


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [ [0]*(n+1) for _ in range(n+1) ]
        for i in range(n):
            dp[1][i] = 1
        for i in range(2,n+1): # 'i' is the length of the pallandrome
            for j in range(n+1-i): # 'j' is where it starts which is why we subract 'i'
                if s[j] == s[i+j-1]:
                    dp[i][j] = 2 + dp[i-2][j+1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
        return dp[n][0]