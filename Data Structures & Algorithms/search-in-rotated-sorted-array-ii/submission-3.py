class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
           
            while l < r and nums[l] == nums[r]:
                l += 1
                r -= 1
            

            if nums[l] <= nums[m]:  # Left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:  # Right portion
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False

# 0,1,2,3,4
# 1,0,1,1,1
# l = 1, r = 3
# m = 2












