class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = -1
        l, r = 0, 0
        mpp = {}
       
        if len(s)==0:
            return 0
        while r < len(s):
            if s[r] in mpp:
                if mpp[s[r]] >= l:
                    l = mpp[s[r]]+1
            mpp[s[r]] = r
            ans = max(ans, r-l+1)
            r += 1
        return ans



        