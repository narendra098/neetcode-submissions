class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}
        def dfs(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if i1 > m-1 or i2 > n-1:
                return 0
            if i1 == m-1 and i2 == n-1:
                return 1
            dp[(i1, i2)] = dfs(i1+1, i2) + dfs(i1, i2+1)
            return dp[(i1, i2)]
            
        return dfs(0, 0)


        
        