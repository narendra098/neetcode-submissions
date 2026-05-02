class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}
        def dfs(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if i1 > m-1 or i2 > n-1:
                return float('inf')
            if i1 == m-1 and i2 == n-1:
                return grid[i1][i2]
            dp[(i1, i2)] = grid[i1][i2] + min(dfs(i1+1, i2) , dfs(i1, i2+1))
            return dp[(i1, i2)]
            
        return dfs(0, 0)


        