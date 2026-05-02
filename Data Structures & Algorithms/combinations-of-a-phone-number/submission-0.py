class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mpp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def dfs(i, res):
            if len(res) == len(digits):
                ans.append(res)
                return 
            
            for ch in mpp[digits[i]]:
                dfs(i+1, res+ch)
        if digits:
            dfs(0, '')
        return ans        