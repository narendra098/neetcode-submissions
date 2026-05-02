class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums)-1):
            num = prefix[-1]*nums[i]
            prefix.append(num)
      
        suffix = [1]
        for i in range(len(nums)-1, 0, -1):
            num = suffix[-1]*nums[i]
            suffix.append(num)
        suffix = suffix[::-1]
      
        ans = []
        for i in range(len(prefix)):
            num = prefix[i]*suffix[i]
            ans.append(num)
        return ans