class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = -1
        l, r = 0, 0
        mpp = {}
       
        if len(s)==0:
            return 0
        while r < len(s):
            if s[r] in mpp:
                l = max(mpp[s[r]]+1, l)
            mpp[s[r]] = r
            ans = max(ans, r-l+1)
            r += 1
        return ans



        