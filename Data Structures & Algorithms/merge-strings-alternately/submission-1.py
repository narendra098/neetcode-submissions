class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        l, r = 0, 0

        while l < len(word1) or r < len(word2):
            if l == len(word1):
                return res+word2[r:]
            if r == len(word2):
                return res+word1[l:]

            res += word1[l]
            res += word2[r]
            l += 1
            r += 1

        return res        