class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            b=nums.count(i)
            if b==1:
                return i

                
            
        