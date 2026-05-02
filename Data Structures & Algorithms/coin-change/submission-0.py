class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(idx, rem):
            if idx == len(coins):
                return 0 if rem == 0 else float('inf')
            
            if (idx, rem) in cache:
                return cache[(idx, rem)]

            take = float('inf')
            if coins[idx] <= rem:
                take = 1 + dp(idx, rem-coins[idx])
            skip = dp(idx+1, rem)
            cache[(idx, rem)] = min(take, skip)
            return cache[(idx, rem)]
        
        ans = dp(0, amount)
        if ans != float('inf'):
            return int(ans) 
        else:
            return -1
