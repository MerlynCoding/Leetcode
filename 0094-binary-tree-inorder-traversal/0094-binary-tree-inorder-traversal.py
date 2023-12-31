# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None
class Solution(object):
    def inorderTraversal(self, root):
        result=[]

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
    
        inorder(root)
        return result

        