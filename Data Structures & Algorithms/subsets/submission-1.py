class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def subs(i, res):
            if i >= len(nums):
                ans.append(res)
                return 
            subs(i+1, res)
            subs(i+1, res+[nums[i]])
        subs(0, [])
        return ans
        