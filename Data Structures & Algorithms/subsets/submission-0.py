class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(res, idx):
            if idx >= len(nums):
                ans.append(res)
                return 
            dfs(res, idx+1)
            dfs(res+[nums[idx]], idx+1)

        dfs([], 0)
        return ans        