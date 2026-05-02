class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            # base case 
            if j < 0:
                return 1
            if i < 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            # what if it matches 
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i-1, j-1) + dfs(i-1, j)
                return dp[(i, j)]

            # what if it don't match 
            dp[(i, j)] = dfs(i-1, j)
            return dp[(i, j)]
        
        return dfs(len(s)-1, len(t)-1)
