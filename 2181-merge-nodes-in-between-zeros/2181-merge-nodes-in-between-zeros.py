# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp = head.next # find first node that isn't 0
        curr = temp # make a copy for traversing
        
        while curr:
            sum_val = 0 # sum of values for merge
            
            while curr.val != 0:
                sum_val += curr.val
                curr = curr.next
            
            temp.val = sum_val
            curr = curr.next
            temp.next = curr
            temp = curr
        
        return head.next
            
            