class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(nums, idx, tar, res):
            if idx >= len(nums):
                if tar == 0:
                    ans.append(res)
                return 
            if nums[idx] <= tar:
                helper(nums, idx, tar-nums[idx], res + [nums[idx]])
            helper(nums, idx+1, tar, res)
        helper(nums, 0, target, [])
        return ans