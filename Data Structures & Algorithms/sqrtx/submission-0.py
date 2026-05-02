class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if mid*mid == x:
               return mid
            elif mid*mid < x:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1 
        return ans

        # x = sqrt(9)
        # x^2 = 9
        # 9
        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        # 0 and 13
        # mid = 6 
        # mid*mid = 36
        # l = 0, r = 5
        # mid = 2
        # mid*mid = 4
        # 
        # l = 3, r = 5
        # mid = 4
        # mid*mid = 16
        #
        # l=3, r = 3
        # mid*mid = 9
        # 
            
        