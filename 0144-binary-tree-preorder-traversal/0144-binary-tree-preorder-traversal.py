# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return[]
        
        result=[]
        stack=[root]

        while stack:
            current_node = stack.pop()
            result.append(current_node.val)

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return result
        