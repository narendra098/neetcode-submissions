class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def helper(cdts, idx, tar, res):
            if tar == 0:
                ans.append(res)
                return
            for i in range(idx, len(cdts)):
                if i > idx and cdts[i] == cdts[i-1]:
                    continue
                if  cdts[i] > tar:
                    break
                
                helper(cdts, i+1, tar-cdts[i], res+[cdts[i]])
                

        helper(candidates, 0, target, [])

        return ans