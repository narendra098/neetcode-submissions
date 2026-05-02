import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def noOfDaysTakes(capacity):
            d = 1
            curr_cap = 0
            for w in weights:
                if curr_cap + w > capacity:
                    curr_cap = w
                    d += 1
                else:
                    curr_cap += w
            return d
        
        l, r = max(weights), sum(weights)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if noOfDaysTakes(mid) <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return l
    