import math
class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ans lies between min and max of piles so l = min, r = max 
        # calc mid and check if mid fits for the ans 
        # if r increases can eat in less time
        # if calc(mid) > h: l = mid + 1
        # if calc(mid) < h: r = mid - 1 => store mid in ans
        def calcNumberOfHours(mid):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            return hours

        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if calcNumberOfHours(mid) <= h:
                ans = mid 
                r = mid - 1 
            else:
                l = mid + 1
        return ans


        