# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        total=dummy
        front=0
        back=0
        while l1 or l2 or back:
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0
            plus=l1_val+l2_val+back
            front=plus%10
            new_node=ListNode(front)
            total.next=new_node
            total=total.next
            back=plus//10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next

        