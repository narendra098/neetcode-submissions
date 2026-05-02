from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = defaultdict(int)
        for i in range(len(nums)):
            rem = target - nums[i] 
            if rem in mpp:
                return [mpp[rem], i]     
            mpp[nums[i]] = i
    


        
        