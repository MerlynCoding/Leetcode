class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:]=nums1[:m]
        nums1[:]+=nums2
        nums1[:]=sorted(nums1)
        return nums1
        