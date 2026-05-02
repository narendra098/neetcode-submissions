class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mpp = {}

        for s in strs:
            k = [0]*26
            for ch in s:
                k[ord(ch)-ord('a')] += 1
            strk = str(k)
            if strk in mpp:
                mpp[strk].append(s)
            else:
                mpp[strk] = [s]
        return list(mpp.values())
        