class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = float('inf')
        maxpr = float('-inf')
        for pr in prices:
            minsofar = min(pr, minsofar)
            maxpr = max(maxpr, pr - minsofar)
        return maxpr

        