class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            curr = nums[i]
            if curr > 0:
                break
            if i > 0 and curr == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                curr_sum = nums[l]+nums[r]
                if curr_sum + curr > 0:
                    r -= 1
                elif curr_sum + curr < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans


        