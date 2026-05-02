class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def genPar(s, op=0, cl=0):
            if len(s) == 2*n:
                ans.append(s)
                return
            if op < n:
                genPar(s+"(", op+1, cl)
            if cl < op:
                genPar(s+")", op, cl+1)
        
        genPar("")
        return ans