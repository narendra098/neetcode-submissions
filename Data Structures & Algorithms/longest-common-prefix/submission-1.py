class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for s in strs:
            if not s:
                return ""

        shortest_len = min(len(s) for s in strs)

        for i in range(shortest_len):
            ch = strs[0][i]
            if any(s[i] != ch for s in strs[1:]):
                return strs[0][:i]
            
        return strs[0][:shortest_len]
