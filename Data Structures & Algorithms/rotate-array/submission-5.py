class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rt(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
    
        k = k %  len(nums)        
        rt(0, len(nums)-1)        
        rt(0, k-1) 
        rt(k, len(nums)-1)