class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def dp(sub, tar, idx):
            if tar==0:
                res.append(sub)
                return
            if idx >= len(nums) or tar < 0:
                return     
            dp(sub+[nums[idx]], tar-nums[idx], idx)
            dp(sub, tar, idx+1)

        dp([], target, 0)
        return res

        