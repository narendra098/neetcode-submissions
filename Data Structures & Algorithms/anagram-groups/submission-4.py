class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for s in strs:
            key = [0]*26
            for ch in s:
                key[ord(ch)-ord('a')] += 1
            if tuple(key) not in mpp:
                mpp[tuple(key)] = [s]
            else:
                mpp[tuple(key)].append(s)
        res = []
        for r in mpp.values():
            res.append(r)
        return res