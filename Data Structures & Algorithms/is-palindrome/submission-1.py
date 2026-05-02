class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            print("l: ", s[l], "r: ", s[r])
            if s[l].isalnum() and s[r].isalnum():
                left_c = s[l].lower()
                right_c = s[r].lower()
                if left_c != right_c:
                    return False
                else:
                    l += 1
                    r -= 1
            if s[l].isalnum() == False:
                l += 1
            if s[r].isalnum() == False:
                r -= 1
        return True
        