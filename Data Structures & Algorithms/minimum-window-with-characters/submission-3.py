class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        mpp_t = {}
        for ch in t:
            mpp_t[ch] = 1 + mpp_t.get(ch, 0)
        mpp_s = {}
        have, need = 0, len(mpp_t)
        res, resLen = [-1, -1], float('infinity')
        for r in range(len(s)):
            mpp_s[s[r]] = 1 + mpp_s.get(s[r], 0)
            if s[r] in mpp_t and mpp_t[s[r]] == mpp_s[s[r]]:
                have += 1
            while need == have:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                mpp_s[s[l]] -= 1
                if s[l] in mpp_t and mpp_s[s[l]] < mpp_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l: r+1] if resLen != float('infinity') else ''
