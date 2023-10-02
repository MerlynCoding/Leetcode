class Solution(object):
    def searchInsert(self, nums, target):
        nums.append(target)
        return sorted(nums).index(target)
        