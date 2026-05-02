class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # go through each row 
        # check if row[0] < tar < row[-1]
        # if true: return  binsearch(row, tar)

        def bin_search(row, tar):
            l, r = 0, len(row)-1
            while l <= r:
                mid = (l+r)//2
                if row[mid]==tar:
                    return True
                elif row[mid] < tar:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        for row in matrix:
            if row[0] <= target and row[-1]>=target:
                return bin_search(row, target)
        
        return False

        