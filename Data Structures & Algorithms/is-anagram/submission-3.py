class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp = [0]*26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            mpp[ord(s[i])-ord('a')] += 1
            mpp[ord(t[i])-ord('a')] -= 1
        
        for num in mpp:
            if num != 0:
                return False
        return True
