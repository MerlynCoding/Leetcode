# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def insert(self,a,i):
        
        
        if a is None:
            a=TreeNode(i)
            return a
        if i<a.val:
            a.left=self.insert(a.left,i)
        else:
            a.right=self.insert(a.right,i)
        return a

            

    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
            
                


                
        