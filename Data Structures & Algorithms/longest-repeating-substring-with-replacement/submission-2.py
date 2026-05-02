class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        mpp = {}
        max_char_freq = -1
        ans = -1
        while r < len(s):
            mpp[s[r]] = 1 + mpp.get(s[r], 0)
            if mpp[s[r]] > max_char_freq:
                max_char_freq = mpp[s[r]]
            

            while (r-l+1)-max_char_freq > k:
                mpp[s[l]] -= 1
                if mpp.get(s[l])==0:
                    del mpp[s[l]]
                max_char_freq = max(mpp.values())
                l += 1
            else:
                ans = max(ans, r-l+1)
            r += 1
        return ans
                 

        
        