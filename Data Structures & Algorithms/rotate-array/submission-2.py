class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        def revsub(l, r, nums):
            # 1 2 3 4 5 6 7 
            # 
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        revsub(0, len(nums)-1, nums)
        revsub(0, k-1, nums)
        revsub(k, len(nums)-1, nums)

        
        