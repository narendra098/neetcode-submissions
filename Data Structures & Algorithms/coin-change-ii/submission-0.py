class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(idx, rem):
            if (idx, rem) in dp:
                return dp[(idx, rem)]
            if rem == 0:
                return 1
            if idx == len(coins):
                return 0
            take = 0
            if coins[idx] <= rem:
                take =  dfs(idx, rem-coins[idx])
            skip = dfs(idx+1, rem)
            dp[(idx, rem)]=take+skip
            return dp[(idx, rem)]
        
        return dfs(0, amount)
        