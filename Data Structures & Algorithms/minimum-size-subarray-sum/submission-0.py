class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        till_sum = 0
        res = float('inf')
        while r < len(nums):
            till_sum += nums[r]
            while till_sum >= target:
                res = min(r-l+1, res)
                till_sum -= nums[l]
                l += 1
            r += 1
        return 0 if res == float('inf') else res


        