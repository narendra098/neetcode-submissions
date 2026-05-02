from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
# AAABBCCD
        mpp = defaultdict(int)
        l = 0
        maxf = 0
        ans = 0

        for r in range(len(s)):
            mpp[s[r]] += 1
            maxf = max(maxf, mpp[s[r]])
            while (r - l + 1) - maxf > k:
                mpp[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans

    # ans = 3, maxf = 3
    # 0 1 2 3 4 5 6 7
    # A A A B B C C D 
    #   l       r
    # mpp = A:3, B:2, C:1

        