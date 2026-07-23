class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for ch in s:
            smap[ch] = 1 + smap.get(ch, 0)
        
        for ch in t:
            tmap[ch] = 1 + tmap.get(ch, 0)
        
        return smap == tmap
        