class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    # if num > 0: swap nums[i] and nums[nums[i]-1]
    # then scan from start if at any index wrong number is there then idx+1 is the answer
        n = len(nums)
        i = 0
        while i < n:
            if nums[i]>0 and nums[i] < len(nums):
                element = nums[i] #4
                chair = element - 1 #3
                if nums[chair] != element:
                    e1 = nums[i]
                    e2 = nums[nums[i]-1]
                    nums[i] = e2 
                    nums[e1-1] = e1
                    i -= 1
            i += 1
    
    # 0 1 2 3 4 5 6 
    # 1 2 4 5 6 3 1     
    # 1 2 5 4 6 3 1
    # 1 2 6 4 5 3 1
    # 1 2 3 4 5 6 1   
        
        if nums[-1] == len(nums):
            return len(nums)+1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1


    

        