# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def max1(self, p, q, a):
        if p is None and q is None:
            return a
        if p is None:
            a += 1
            return self.max1(q.right, q.left, a)
        if q is None:
            a += 1
            return self.max1(p.right, p.left, a)

        left_depth = self.max1(p.left, q.right, a)
        right_depth = self.max1(p.right, q.left, a)
        return max(left_depth, right_depth) + 1

    def maxDepth(self, root):
        a = 0
        if root is None:
            return a
        return self.max1(root.left, root.right, a)+1
