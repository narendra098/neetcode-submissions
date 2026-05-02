class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = len(min(strs, key=len))
        ptr = 0
        while ptr < minlen:
            chr = strs[0][ptr]
            for i in range(1, len(strs)):
                if strs[i][ptr] != chr:
                    return strs[0][:ptr]
            ptr+=1
        
        return strs[0][:ptr]