class Solution:
    def merge(self, nums1, m, nums2, n):
        # pointers
        i = m - 1      # last element in nums1's initial part
        j = n - 1      # last element in nums2
        k = m + n - 1  # last position in nums1

        # merge from the back
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # 10, 20, 20, 40, 0, 0 and 1, 2
