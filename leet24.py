# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead=ListNode(0)
        newhead.next=head
        temp=newhead
        
        while temp.next !=None and temp.next.next !=None:
            p1=temp.next
            p2=p1.next
            
            
            p1.next=p2.next
            p2.next=p1
            temp.next =p2
            temp = p1
        return newhead.next
        
