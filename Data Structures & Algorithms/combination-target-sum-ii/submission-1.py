class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dp(idx, path, curr):
            if curr == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if curr + candidates[i] > target:
                    break
                dp(i+1, path+[candidates[i]], curr+candidates[i])
        dp(0, [], 0)
        return res
            
        