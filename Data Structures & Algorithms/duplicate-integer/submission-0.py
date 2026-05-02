class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = len(set(nums))
        return not a == b
        