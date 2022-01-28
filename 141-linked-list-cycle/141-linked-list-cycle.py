# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        hashing = set()
        isCycle = False
        
        while head:
            data = hash(head)
            
            if data in hashing:
                isCycle = True
                break
            else:
                hashing.add(data)
                
            head = head.next
                
        return isCycle
        