class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def dfs(i1, i2):

            if (i1, i2) in dp:
                return dp[(i1, i2)]
                
            if i1 < 0 or i2 < 0:
                return 0

            if text1[i1]==text2[i2]:
                dp[(i1, i2)] = 1 + dfs(i1-1, i2-1)
                return dp[(i1, i2)]
            else:
                dp[(i1, i2)] = max(dfs(i1, i2-1), dfs(i1-1, i2))
                return dp[(i1, i2)]
        
        return dfs(len(text1)-1, len(text2)-1)
