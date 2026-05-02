class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp = {0:1}
        sofarsm = 0
        cnt = 0
        for num in nums:
            sofarsm += num 
            rem = sofarsm - k 
            cnt += mpp.get(rem, 0)
            mpp[sofarsm] = 1 + mpp.get(sofarsm, 0)
        return cnt


            
            


        
        