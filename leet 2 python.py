# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        iter=1
        tens=0
        ptens=0
        snum=0
        nn=ListNode(0)
        now=nn
        while True:

            num = l1.val+l2.val+ptens
            snum=num%10
            tens=num/10
            now.next=ListNode(snum)
            ptens=tens
            now=now.next
            if l1.next == None and l2.next == None and ptens ==0:
                break
            if l1.next is None: 
                l1.val=0
            else:
                l1=l1.next
            if l2.next is None:
                l2.val=0
            else:
                l2=l2.next
            
        return nn.next
                
            
        
        
        
