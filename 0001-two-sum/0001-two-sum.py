class Solution(object):
    def twoSum(self, nums, target):
        answer=[]
        for i in range(len(nums)):
            ranged=target-nums[i]
            if ranged in nums and nums.index(ranged)!=i :
                
                answer+=[i,nums.index(ranged)]
                return sorted(answer)
                break
            


        