# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)

        if lh==0 or rh==0:
            return max(lh,rh)+1
        return min(lh,rh)+1
        