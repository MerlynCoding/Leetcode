# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        lengthA = get_length(headA)
        lengthB = get_length(headB)

        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1

        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA 
