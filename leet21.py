# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # indexs: l1r, l1l,l2r,l2l, ans=[]
        # recursion solution

        def merge(L1,L2):
            if L1==None:
                return L2
            if L2==None:
                return L1
            if L2.val <=L1.val:
                L2.next=merge(L1,L2.next)
                return L2
            else:
                L1.next=merge(L1.next,L2)
                return L1
        return merge(l1,l2)
        
        # scan solution
        
        ans = ListNode(0)
        temp=ans
            
        while l1 != None and l2 != None:
            if l2.val <=l1.val:
                temp.next=l2
                l2=l2.next
            else:
                temp.next=l1
                l1=l1.next
            temp=temp.next
        if l1 != None:
            temp.next=l1
        else:
            temp.next=l2
        return ans.next
            
        
        # while l1.next != None and L2.next!=None:
        #     while L2.next !=None and l2.val <=l1.val:
        #         ans.append(l2.val)
        #         l2=l2.next
        #     ans.append(l1,=l1.val)
        #     l1=l1.next
        # return ans

                
                    
