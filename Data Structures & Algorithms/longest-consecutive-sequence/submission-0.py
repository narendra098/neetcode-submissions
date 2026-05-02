class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in nums:
            # check if num is the first one or not 
            if num-1 not in numset:
                curr = num
                curr_len = 0
                while curr in numset:
                    curr_len += 1
                    curr += 1
                    ans = max(ans, curr_len)
        return ans

        