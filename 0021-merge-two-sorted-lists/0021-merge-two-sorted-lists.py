# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list3=ListNode(None)
        dumb=list3
        while list1 and list2:
            if list1.val<= list2.val:
                dumb.next=list1
                list1=list1.next
            else:
                dumb.next=list2
                list2=list2.next
            dumb=dumb.next
        

        if list1==None : 
            dumb.next=list2
        elif list2==None :
            dumb.next=list1
    
        return list3.next


        
        