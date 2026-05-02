class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 
        # max = 3
        # l = 1, r = 5, 
        # {z:0, x:1, y:2 
        ans = 0
        l, r = 0, 0
        mpp = {}

        while r < len(s):
            if s[r] in mpp and mpp[s[r]] >= l:
                l = mpp[s[r]] + 1
            
            mpp[s[r]] = r
            winlen = r - l + 1
            ans = max(ans, winlen)
            r += 1
        return ans

# 0 1 2 3 4 5 6 7 8
# c a d b z a b c d 
# mpp = c:0, a:5, d:2, b:6, z;4, 
# l = 4, r = 7
# max = 5

        
        