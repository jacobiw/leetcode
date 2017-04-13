# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        tarL=head
        tarR=tarL
        for i in xrange(n):
            tarR=tarR.next
        if tarR == None:
            head=head.next
            return head
        # n=1
        while head != None:
            if tarR.next == None:
                if n ==1:
                    tarL.next=None
                    return head
                tarL.next = tarL.next.next
                return head
            tarR= tarR.next
            tarL= tarL.next
            
            
            #foster alg
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointer = ListNode(0)
        pointer.next=head
        tarL=pointer
        
        for i in xrange(n):
            head=head.next
        while head != None:
            # searching
            head=head.next
            tarL= tarL.next
        tarL.next = tarL.next.next
        return pointer.next
                
            
