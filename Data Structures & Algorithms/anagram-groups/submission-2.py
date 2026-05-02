class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for s in strs:
            key = [0]*26
            for ch in s:
                key[ord(ch)-97] += 1 
            key_str = "".join([str(val)+"," for val in key])
            if key_str in mpp:
                mpp[key_str].append(s)
            else:
                mpp[key_str] = [s]
        
        return list(mpp.values())
        