class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        ans = []
        while r <= len(nums):
            win = nums[l:r]
            ans.append(max(win))
            r += 1
            l += 1
        
        return ans





        