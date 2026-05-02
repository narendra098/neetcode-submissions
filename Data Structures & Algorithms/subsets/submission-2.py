class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def subs(sub, idx):
            if idx == len(nums):
                ans.append(sub)
                return 
            subs(sub+[nums[idx]], idx+1)
            subs(sub, idx+1)
        
        subs([], 0)
        return ans

        