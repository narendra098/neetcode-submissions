class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(idx, nums, k, res):
            
            if len(res) == k:
                ans.append(res)
                return 
            for i in range(idx, len(nums)):
                dfs(i+1, nums, k, res+[nums[i]])
        
        dfs(0, [i for i in range(1, n+1)], k, [])
        return ans
            

                
        