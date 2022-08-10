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
        visited_set = []
        
        while head:
            if head not in visited_set:
                visited_set.append(head)
            else:
                return True
            
            head = head.next
        
        return False