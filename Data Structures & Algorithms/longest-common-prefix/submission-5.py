class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = len(min(strs, key=len))
        for i in range(minlen):
            if any(strs[0][i] != word[i] for word in strs[1:]):
                return strs[0][:i]
        return strs[0][:minlen]
            
            