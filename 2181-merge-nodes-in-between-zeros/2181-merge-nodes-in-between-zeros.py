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
        
        temp = head.next
        curr = temp
        
        while curr:
            counter = 0
            
            while curr.val != 0:
                counter += curr.val
                curr = curr.next
            
            temp.val = counter
            curr = curr.next
            temp.next = curr
            temp = temp.next
        
        return head.next
            