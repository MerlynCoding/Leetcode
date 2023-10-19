# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self,; val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        current=root
        result=[]
        stack=[]
        while current or stack:
            if current:
                stack.append(current)
                result.append(current.val)
                current=current.right
            else:
                current=stack.pop()
                current=current.left
        return result[::-1]